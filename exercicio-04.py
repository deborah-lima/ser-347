#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt

pop_masculina = [7016987,7624144,8725413,8558868,8630229,8460995,7717658,6766664,6320568,5692014,4834995,3902344,3041035,2224065,1667372,1090517,668623,310759,114964,31529,7247]
pop_feminina= [6779171,7345231,8441348,8432004,8643419,8614963,8026854,7121915,6688796,6141338,5305407,4373877,3468085,2616745,2074264,1472930,998349,508724,211594,66806,16989]
idade = ['0-4', '5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95-99','+100']

plt.figure(figsize=(15,10))

plt.subplot(1,2,1)
plt.barh(idade, pop_masculina, color="blue")

plt.legend(["População Masculina"]);

#Ivertendo o eixo de população masculina
plt.gca().invert_xaxis()

# Tirar os rótulos do eixo lateral
plt.gca().axes.yaxis.set_ticklabels([])

plt.subplot(1,2,2)
plt.barh(idade, pop_feminina, color ="orange")


#plt.barh(idade, pop_masculina);
#plt.barh(idade,pop_feminina,color='gray')


plt.suptitle ("Distribuição da população brasileira",fontsize=16)
plt.legend(["População Feminina"]);

plt.show


# In[ ]:




