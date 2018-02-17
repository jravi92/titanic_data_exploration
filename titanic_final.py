import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


titanic_df=pd.read_csv('titanic-data.csv')

print titanic_df.head()
print titanic_df.groupby('Survived').mean()

print titanic_df.describe()




############# Age Distribution Plot ##########################
age_distribution=titanic_df['Age'][titanic_df['Age']<100]

fig_age, a1=plt.subplots()
graph_m=a1.hist(age_distribution,50)
a1.set_ylabel('Number of Passengers')
a1.set_xlabel('Age in years')
a1.set_title('Age distribution of Passengers')






#grouping the age into 4 section, 1=children(upto 12 years), 2=teen(13 to 19 years)
#3=adult(20 to 40), 4=old(more than 41)

def age_group(age):
    if (age>40):
        return 4
    if ((age<=40) & (age>19)):
        return 3
    if ((age<=19) & (age>12)):
        return 2
    if (age<=12):
        return 1

    
def age_group_all(age):
    return age.apply(age_group)

temp=titanic_df
temp['Age']=age_group_all(titanic_df['Age'])

############## age data filtering into groups ###########################
filter1=temp.fillna('Age'==0)


# Studying data based on gender
male_data= filter1[filter1['Sex']== 'male']
female_data=filter1[filter1['Sex'] == 'female']
print "\nSex data:"
print "     Total Survived Dead"
print "Male:  ",len(male_data),len(male_data[male_data['Survived']==1]),len(male_data[male_data['Survived']==0])
print "Female:",len(female_data),len(female_data[female_data['Survived']==1]),len(female_data[female_data['Survived']==0])

# Analysing data based on age i.e. child or adults 
child_data=filter1[(filter1['Age']==1) | (filter1['Age']==2)]
adult_data=filter1[(filter1['Age']==3) | (filter1['Age']==4)]
print "\nChild Data:"
print "Total Survived Dead"
print len(child_data),len(child_data[child_data['Survived']==1]),len(child_data[child_data['Survived']==0])
print len(adult_data),len(adult_data[adult_data['Survived']==1]),len(adult_data[adult_data['Survived']==0])


# Analysing missing age data, categorizing them in a separate group
missing_age_data=filter1[filter1['Age']==0]
print "\nMissing Age Data:"
print "Total Survived Dead"
print len(missing_age_data),len(missing_age_data[missing_age_data['Survived']==1]),len(missing_age_data[missing_age_data['Survived']==0])

# Filtering data based on Embarkation
embark_S=filter1[filter1['Embarked']=='S']
embark_C=filter1[filter1['Embarked']=='C']
embark_Q=filter1[filter1['Embarked']=='Q']

print "\nEmbark Data:"
print "Total Survived Dead Percentage"
print "S",len(embark_S),len(embark_S[embark_S['Survived']==1]),len(embark_S[embark_S['Survived']==0]),float(len(embark_S[embark_S['Survived']==1]))/len(embark_S)
print "C",len(embark_C),len(embark_C[embark_C['Survived']==1]),len(embark_C[embark_C['Survived']==0]),float(len(embark_C[embark_C['Survived']==1]))/len(embark_C)
print "Q",len(embark_Q),len(embark_Q[embark_Q['Survived']==1]),len(embark_Q[embark_Q['Survived']==0]),float(len(embark_Q[embark_Q['Survived']==1]))/len(embark_Q)

# Filtering data based on Passenger Class

Pclass_1=filter1[filter1['Pclass']==1]
Pclass_2=filter1[filter1['Pclass']==2]
Pclass_3=filter1[filter1['Pclass']==3]

print "\nPclass Data:"
print "Total Survived Dead Percentage"
print "1st Class",len(Pclass_1),len(Pclass_1[Pclass_1['Survived']==1]),len(Pclass_1[Pclass_1['Survived']==0]),float(len(Pclass_1[Pclass_1['Survived']==1]))/len(Pclass_1)
print "2nd Class",len(Pclass_2),len(Pclass_2[Pclass_2['Survived']==1]),len(Pclass_2[Pclass_2['Survived']==0]),float(len(Pclass_2[Pclass_2['Survived']==1]))/len(Pclass_2)
print "3rd Class",len(Pclass_3),len(Pclass_3[Pclass_3['Survived']==1]),len(Pclass_3[Pclass_3['Survived']==0]),float(len(Pclass_3[Pclass_3['Survived']==1]))/len(Pclass_3)



################# Gender plot ################################ 
male_s=male_data['Sex'][male_data["Survived"]==1].count()
male_d=male_data['Sex'][male_data["Survived"]==0].count()

female_s=female_data['Sex'][female_data["Survived"]==1].count()
female_d=female_data['Sex'][female_data["Survived"]==0].count()

N=2
male=(male_s,male_d)
female=(female_s,female_d)

ind=np.arange(N)
width=0.35

fig, ax=plt.subplots()
graph_m=ax.bar(ind, male, width, color='b')
graph_f=ax.bar(ind+width, female, width, color='m')

ax.set_ylabel('Number of Survivals and Deaths')
ax.set_title('Numbers based on Gender')
ax.set_xticks(ind+width/2)
ax.set_xticklabels(('Survived','Deads'))

ax.legend((graph_m[0],graph_f[0]),('Male','Female'))


###############################################################


##################  Age Groups ##########################
children_s=len(  filter1[ (filter1['Age']==1) & (filter1['Survived']==1) ])
teen_s=len(filter1[ (filter1['Age']==2) & (filter1['Survived']==1) ])
adult_s=len(filter1[ (filter1['Age']==3) & (filter1['Survived']==1) ])
old_s=len(filter1[ (filter1['Age']==4) & (filter1['Survived']==1) ])


children_d=len( filter1[(filter1['Age']==1) & (filter1["Survived"]==0)])
teen_d=len(filter1[(filter1['Age']==2) & (filter1["Survived"]==0)])
adult_d=len(filter1[(filter1['Age']==3) & (filter1["Survived"]==0)])
old_d=len(filter1[(filter1['Age']==4) & (filter1["Survived"]==0)])


N=4
group_s=(children_s,teen_s,adult_s,old_s)
group_d=(children_d,teen_d,adult_d,old_d)


ind=np.arange(N)
width=0.2

fig2, bx=plt.subplots()
graph_s=bx.bar(ind, group_s, width, color='g')
graph_d=bx.bar(ind+width, group_d, width, color='r')


bx.set_ylabel('Number of Survivals and Deaths')
bx.set_title('Numbers based on Age Groups')
bx.set_xticks(ind+width/2)
bx.set_xticklabels(('Kids','Teens','Adults','Olds'))

bx.legend((graph_s[0],graph_d[0]),('Survived','Dead'))

#################################################################


###################### Passenger Class ##########################

pclass_s1=len(Pclass_1[Pclass_1['Survived']==1])
pclass_s2=len(Pclass_2[Pclass_2['Survived']==1])
pclass_s3=len(Pclass_3[Pclass_3['Survived']==1])

pclass_d1=len(Pclass_1[Pclass_1['Survived']==0])
pclass_d2=len(Pclass_2[Pclass_2['Survived']==0])
pclass_d3=len(Pclass_3[Pclass_3['Survived']==0])

N=3
group_s=(pclass_s1,pclass_s2,pclass_s3)
group_d=(pclass_d1,pclass_d2,pclass_d3)


ind=np.arange(N)
width=0.2

fig3, cx=plt.subplots()
graph_s=cx.bar(ind, group_s, width, color='g')
graph_d=cx.bar(ind+width, group_d, width, color='r')


cx.set_ylabel('Number of Survivals and Deaths')
cx.set_title('Numbers based on Passenger Class')
cx.set_xticks(ind+width/2)
cx.set_xticklabels(('Pclass 1','Pclass 2','Pclass 3'))

cx.legend((graph_s[0],graph_d[0]),('Survived','Dead'))


plt.show()



