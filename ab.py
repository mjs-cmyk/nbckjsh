#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���ɽ
���ڣ�
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
6
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    pass #��дִ�д���,������ɺ�passɾ��
    if name == "rock":
        name = 0
        return name

    elif name == "spock":
        name = 1
        return name

    elif name == "paper":
        name = 2
        return name

    elif name == "lizard":
        name = 3
        return name

    elif name == "scissors":
        name = 4
        return name
    else:
        print('Errror:No correct Name')
        name = -1
        return name
       


    



def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    pass #��дִ�д���,������ɺ�passɾ��
    if number == 0:
        number = "rock"
        return number

    elif number == 1:
        number = "spock"
        return number

    elif number == 2:
        number = "paper"
        return number

    elif number == 3:
        number = "lizard"
        return number

    elif number == 4:
        number = "scissors"
        return number
    


def rpsls(choice_name):
    
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass
    
 
    comp_number = random.randrange(5)
    
    while(name_to_number(choice_name) == -1):
        print ("please enter again")
        choice_name=input() 
  
    player_number = name_to_number(choice_name)
    print("Player choice is: " + choice_name)

    print("Computer choice is: " + number_to_name(comp_number))

    difference = (int(player_number) - comp_number) % 5

    draws = 0

    playerwins = 0

    computerwins = 0
    
    if difference in [1, 2]:
        print ("Player wins!")
        choice_name=input() 
        rpsls(choice_name)



    elif difference == 0:
        print ("Player and computer tie!")
        choice_name=input() 
        rpsls(choice_name)


    else:
        print ("Computer wins!")
        choice_name=input() 
        rpsls(choice_name)
        
   

    

# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input() 
rpsls(choice_name)



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





