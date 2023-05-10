CdAge={'young':{'yes':2/5, 'no':3/5},
       'avg':{'yes':1,'no':0},
       'senior':{'yes':3/5, 'no':2/5}}
CdIncome={
    'low':{'yes':3/4,'no':1/4},
    'medium':{'yes':4/6,'no':2/6},
    'high':{'yes':2/4,'no':2/4}
}
cdStudent={
    'yes':{'yes':6/7,'no':1/7},
    'no':{'yes':3/7,'no':4/7}
}
cdCreditRating={
    'fair':{'yes':6/8,'no':2/8},
    'excellent':{'yes':3/6,'no':3/6}
}

PYes=9/14
PNo=5/14

age=input('Enter Age =young, avg, senior : ')
income=input('Enter income=low, medium, high :')
student=input('Enter student= yes, no : ')
cr=input('Enter credit rating=fair, excellent : ')

VnbYes=PYes*(CdAge[age]['yes'])*CdIncome[income]['yes']*cdCreditRating[cr]['yes']*cdStudent[student]['yes'];

VnbNo=PNo*(CdAge[age]['no'])*CdIncome[income]['no']*cdCreditRating[cr]['no']*cdStudent[student]['no'];
print(VnbYes/(VnbYes+VnbNo));
print(VnbNo/(VnbYes+VnbNo));

if(VnbYes>VnbNo):
  print('Buy computer =yes')
else:
  print('Buy computer=No')