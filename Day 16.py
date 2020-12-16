import DATA
import time


def sort_raw_data(raw_data):
    near_tickets = []
    ticket_fields = {}
    data = raw_data.splitlines()
    extract_data = data.copy()
    for line in extract_data:
        # sport the ranges
        data.remove(line)
        if line == "":
            break
        name, ranges = line.split(": ")
        ranges = ranges.split(" or ")
        ranges_list = []
        ticket_fields[name] = ranges_list
        for range in ranges:
            ticket_fields[name].append(list(map(int, range.split("-"))))
    # sort your ticket
    del data[0]
    my_ticket = eval(data[0])
    del data[:3]
    for line in data:
        near_tickets.append(eval(line))
    return ticket_fields, my_ticket, near_tickets


def check_error_rate(raw_data):
    ticket_fields, my_ticket, near_tickets = sort_raw_data(raw_data)
    field_positions = {}
    for field in ticket_fields:
        field_positions[field] = []
    total_errors = 0
    temp_near_tickets = near_tickets.copy()
    for ticket in temp_near_tickets:
        for num in ticket:
            valid = False
            for ranges in ticket_fields.values():
                if num in range(ranges[0][0], ranges[0][1] + 1):
                    valid = True
                    break
                elif num in range(ranges[1][0], ranges[1][1] + 1):
                    valid = True
                    break
            if not valid:
                total_errors += num
                near_tickets.remove(ticket)
    # work out positions
    for ticket in near_tickets:
        for pos, num in enumerate(ticket):
            for field in ticket_fields:
                for ranges in ticket_fields[field]:
                    if num in range(ranges[0], ranges[1] + 1):
                        field_positions[field].append(pos)
    ticket_amount = len(near_tickets)
    field_amount = len(field_positions)
    for pos in range(field_amount):
        for field in field_positions.keys():
            contents = field_positions[field]
            count = contents.count(pos)
            if count < ticket_amount:
                field_positions[field] = list(filter(lambda a: a != pos, contents))
            else:
                for i in range(ticket_amount - 1):
                    field_positions[field].remove(pos)
    solve_number = 0
    while solve_number != field_amount:
        solve_number = 0
        for field in field_positions:
            if len(field_positions[field]) == 1:
                solve_number += 1
                pos = field_positions[field][0]
                # Delete position from other fields as it can only be in this field
                skip_field = field
                for field in field_positions:
                    if field != skip_field:
                        field_positions[field] = list(filter(lambda a: a != pos, field_positions[field]))
    for field in field_positions:
        print(field, field_positions[field])
    departure_positions = []
    for field in field_positions:
        if "departure" in field:
            departure_positions.append(field_positions[field][0])
    part_2_ans = 1
    for pos in departure_positions:
        part_2_ans = part_2_ans * my_ticket[pos]

    return total_errors, part_2_ans


start = time.time()
part_1, part_2 = check_error_rate(DATA.Day_16)
print("part one ans {}\npart two ans {}".format(part_1, part_2))
end = time.time()
print("ran in {} seconds".format(end - start))