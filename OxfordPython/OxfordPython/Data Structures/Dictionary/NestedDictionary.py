"""
WAP to illustrate nested dictionary (i.e use of one dictionary inside another)

"""

students = {'shiv': {'cs': 90,'ds':89,'csa':92},
            'Sandhvi': {'cs': 94,'ds':49,'csa':22},
            'Krish': {'cs': 93,'ds':59,'csa':92}}

for key,val in students.items():
    print(key,val)