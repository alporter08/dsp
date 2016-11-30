import re
from pprint import pprint

def faculty_dict(file):

    fin = open(file)
    next(fin) #skip first line (header)

    faculty_dict = {}

    for line in fin:
        l = line.split(',')
        l = [x.strip() for x in l]

        # clean names
        names = l[0].split()
        last_name = names[len(names)-1]

        # degrees
        degrees = l[1]

        # clean title
        title = l[2]
        title = re.sub(' .. Biostatistics','',title) # remove ' of Biostatistics'
        # from degrees

        # emails
        emails = l[3]

        if last_name not in faculty_dict:
            faculty_dict[last_name] = [[degrees, title, emails]]
        else:
            faculty_dict[last_name].append([degrees, title, emails])

    return faculty_dict


def professor_dict(file):

        fin = open(file)
        next(fin) #skip first line (header)

        professor_dict = {}

        for line in fin:
            l = line.split(',')
            l = [x.strip() for x in l]

            # clean names
            names = l[0].split()
            last_name = names[len(names)-1]
            first_name = names[0]
            professor = last_name, first_name

            # degrees
            degrees = l[1]

            # clean title
            title = l[2]
            title = re.sub(' .. Biostatistics','',title) # remove ' of Biostatistics'
            # from degrees

            # emails
            emails = l[3]

            if professor not in professor_dict:
                professor_dict[professor] = [degrees, title, emails]
            else:
                professor_dict[professor].append([degrees, title, emails])

        pprint_dict = pprint(professor_dict)

        return pprint_dict
