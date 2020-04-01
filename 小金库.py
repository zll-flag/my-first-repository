import pymssql
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk



def callback(event):
    global IN1
    global IN2
    global IN3
    global IN4
    global IN5
    global IN6
    global IN7
    for item in treeview.selection():
        item_text=treeview.item(item,"values")#选出点击的数据，存入到元组iTem_TexT
    IN1=item_text[0]
    IN2=item_text[1]
    IN3=item_text[2]
    IN4=item_text[3]
    IN5=item_text[4]
    IN6=item_text[5]
    IN7=item_text[6]

    IN1='\''+IN1 +'\''
    IN2='\''+IN2+'\''
    IN4='\''+IN4+'\''
    IN5='\''+IN5+'\''
    IN6='\''+IN6+'\''
    IN7='\''+IN7+'\''
    del item_text[:]
    
        
        
        
        
        
            
           
    
    
def delButton(tree):
    x=tree.get_children()
    for item in x:
        tree.delete(item)

def getstu():
    delButton(treeview)
    print('-----')
    conn = pymssql.connect(host='127.0.0.1',user='gong',password='0810lookout',database='moeny',charset="UTF-8")
    print(conn)##连接是否成功?
    print('连接成功!')    #查看连接是否成功
    cursor = conn.cursor()
    sql = 'select* from information'
    cursor.execute(sql)
    row=cursor.fetchone() #用一个变量获取数据
    while row:
        treeview.insert('','end',values=row)
        row= cursor.fetchone()
    conn.close()
    # rs = cursor.fetchall()
    # print(rs)
def find_num():
    delButton(treeview)
    num=E1.get().strip()
    num='\'%'+num +'%\''
    name=E2.get().strip()
    name='\'%'+name +'%\''
    banlance=E3.get()
    Type=E4.get().strip()
    Type='\'%'+Type+'%\''
    para=E7.get().strip()
    para='\'%'+para+'%\''
    location=E5.get().strip()
    location='\'%'+location+'%\''
    note=E6.get().strip()
    note='\'%'+note+'%\''
    print(len(num))
    conn = pymssql.connect(host='127.0.0.1',user='gong',password='0810lookout',database='moeny',charset="UTF-8")
    cursor = conn.cursor()
    sql='select* from information'
    if len(num)>4:
        sql=sql+' where %s like %s'%('num',num)

    if len(name)>4:
        if(sql.find('where')==-1):
            sql=sql+' where %s like %s'%('name',name)
        else:
            sql=sql+'and %s like %s'%('name',name)

    if len(banlance)>0:
        if(sql.find('where')==-1):
            sql=sql+' where %s like %s'%('banlance',banlance)
        else:
            sql=sql+'and %s like %s'%('banlance',banlance)

    if len(Type)>4:
        if(sql.find('where')==-1):
            sql=sql+' where %s like %s'%('type1',Type)
        else:
            sql=sql+'and %s like %s'%('type1',Type)

    if len(para)>4:
        if(sql.find('where')==-1):
            sql=sql+' where %s like %s'%('para',para)
        else:
            sql=sql+'and %s like %s'%('para',para)

    if len(location)>4:
        if(sql.find('where')==-1):
            sql=sql+' where %s like %s'%('location',location)
        else:
            sql=sql+'and %s like %s'%('location',location)
  
    if len(note)>4:
        if(sql.find('where')==-1):
            sql=sql+' where %s like %s'%('note',note)
        else:
            sql=sql+'and %s like %s'%('note',note)
    print(sql)
    cursor.execute(sql)
    row=cursor.fetchone() #用一个变量获取数据
    while row:
        treeview.insert('','end',values=row)
        row= cursor.fetchone()
    conn.close()
        

def Add():
    delButton(treeview)
    num=E1.get().strip()
    if len(num)==0:
        tk.messagebox.showerror(title='error',message='NUM为空，请输入')
        return
    num='\''+num+'\''
    name= E2.get().strip()
    name='\''+name+'\''
    banlance=E3.get()
    Type=E4.get().strip()
    Type='\''+Type+'\''
    para=E7.get().strip()
    para='\''+para+'\''
    location=E5.get().strip()
    location='\''+location+'\''
    note=E6.get().strip()
    note='\''+note+'\''
    conn = pymssql.connect(host='127.0.0.1',user='gong',password='0810lookout',database='moeny',charset="UTF-8")
    cursor = conn.cursor()
    sql='insert into information(num,name,banlance,type1,para,location,note) values('+num+','+name+','+'\''+banlance+'\''+','+Type+','+para+','+location+','+note+')'
    print(sql)
    try:
        cursor.execute(sql)
        tk.messagebox.showinfo(title='remind',message='成功添加')
    except:
        tk.messagebox.showerror(title='error',message='NUM 重复，请更改')
        
    conn.commit()
    conn.close()
    getstu()
    
    

def delete():
    global IN1
    global IN2
    global IN3
    global IN4
    global IN5
    global IN6
    global IN7
    print(IN1)
   
    delButton(treeview)
    conn = pymssql.connect(host='127.0.0.1',user='gong',password='0810lookout',database='moeny',charset="UTF-8")
    cursor = conn.cursor()
    sql='delete from information'
    if len(IN1)>2:
        sql=sql+' where %s = %s'%('num',IN1)

    '''if len(IN2)>2:
        if(sql.find('where')==-1):
            sql=sql+' where %s = %s'%('name',IN2)
        else:
            sql=sql+'and %s = %s'%('name',IN2)

    if len(IN3)>0:
        if(sql.find('where')==-1):
            sql=sql+' where %s = %s'%('banlance',IN3)
        else:
            sql=sql+'and %s = %s'%('banlance',IN3)

    if len(IN4)>2:
        if(sql.find('where')==-1):
            sql=sql+' where %s = %s'%('type1',IN4)
        else:
            sql=sql+' and %s = %s'%('type1',IN4)
  
    if len(IN5)>2:
        if(sql.find('where')==-1):
            sql=sql+' where %s like %s'%('para',IN5)
        else:
            sql=sql+'and %s like %s'%('para',IN5)
  
    if len(IN6)>2:
        if(sql.find('where')==-1):
            sql=sql+' where %s = %s'%('location',IN6)
        else:
            sql=sql+'and %s = %s'%('location',IN6)
    
    if len(IN7)>2:
        if(sql.find('where')==-1):
            sql=sql+' where %s = %s'%('note',IN7)
        else:
            sql=sql+'and %s = %s'%('note',IN7)'''
    print(sql)
    conn = pymssql.connect(host='127.0.0.1',user='gong',password='0810lookout',database='moeny',charset="UTF-8")
    cursor = conn.cursor()
    if(len(IN1)==0):
        tk.messagebox.showerror(title='error',message='没选择数据')
    else:
        cursor.execute(sql)
        tk.messagebox.showinfo(title='remind',message='删除成功')
    conn.commit()
    conn.close()
    getstu()
    

def change():

    '''tk.messagebox.showinfo(title='remind',message='窗口中双击选中的内容后，输入新内容点击修改')'''
    num=E1.get().strip()
    num='\''+num +'\''
    name=E2.get().strip()
    name='\''+name +'\''
    banlance=E3.get()
    Type=E4.get().strip()
    Type='\''+Type+'\''
    para=E7.get().strip()
    para='\''+para+'\''
    location=E5.get().strip()
    location='\''+location+'\''
    note=E6.get().strip()
    note='\''+note+'\''
    print(len(num))
   
    sql='update information set'
    if len(num)>2:
        sql=sql+',%s = %s'%('num',num)
    if len(name)>2:
            sql=sql+', %s = %s'%('name',name)
    if len(banlance)>0:
            sql=sql+', %s = %s'%('banlance ',banlance)

    if len(Type)>2:
            sql=sql+', %s= %s'%('type1',Type)

    if len(para)>2:
            sql=sql+', %s = %s'%('para',para)

    if len(location)>2:
            sql=sql+', %s= %s'%('location',location)
  
    if len(note)>2:
            sql=sql+', %s= %s'%('note',note)

    print(sql)

    global IN1
    global IN2
    global IN3
    global IN4
    global IN5
    global IN6
    global IN7

    sql2=''
    if len(IN1)>2:
        sql2=sql2+' %s = %s'%('num',IN1)

    '''if len(IN2)>2:
        if(len(sql2)>0):
            sql2=sql2+'and %s = %s'%('name',IN2)
        else:
            sql2=sql2+' %s = %s'%('name',IN2)
     
    if len(IN3)>0:
        if(len(sql2)>0):
            sql2=sql2+'and %s = %s'%('banlance ',IN3)
        else:
            sql2=sql2+' %s = %s'%('banlance ',IN3)

    if len(IN4)>2:
        if(len(sql2)>0):
            sql2=sql2+'and %s= %s'%('type1',IN4)
        else:
            sql2=sql2+' %s= %s'%('type1',IN4)

    if len(IN5)>2:
        if(len(sql2)>0):
            sql2=sql2+'and %s = %s'%('para',IN5)
        else:
            sql2=sql2+'%s = %s'%('para',IN5)

    if len(IN6)>2:
        if(len(sql2)>0):
            sql2=sql2+'and %s= %s'%('location',IN6)
        else:
            sql2=sql2+' %s= %s'%('location',IN6)
  
    if len(IN7)>2:
        if(len(sql2)>0):
            sql2=sql2+'and %s= %s'%('note',IN7)
        else:
            sql2=sql2+'%s= %s'%('note',IN7)'''
    
    SQL=sql+' where '+sql2
    print(SQL)
    SQL=SQL.replace('set,','set ')
    print(SQL)
    conn = pymssql.connect(host='127.0.0.1',user='gong',password='0810lookout',database='moeny',charset="UTF-8")
    cursor = conn.cursor()
    try:
        cursor.execute(SQL)
        tk.messagebox.showinfo(title='remind',message='成功修改')
    except:
        tk.messagebox.showerror(title='error',message='NUM 重复，请更改')
        
    conn.commit()
    conn.close()
    getstu()
    

if __name__ == '__main__':


    window =tk.Tk()
    window.title=("欢迎到小金库")
    window.geometry('600x600')

    columns=("NUM",'NAME','BANLANCE','TYPE','PARA','LOCATINO','NOTE')
    treeview=ttk.Treeview(window,height=10,show="headings",columns=columns)
    treeview.column("NUM",width=80,anchor='center')
    treeview.column("NAME",width=80,anchor='center')
    treeview.column("BANLANCE",width=80,anchor='center')
    treeview.column("TYPE",width=80,anchor='center')
    treeview.column("PARA",width=80,anchor='center')
    treeview.column("LOCATINO",width=80,anchor='center')
    treeview.column("NOTE",width=80,anchor='center')
    
    treeview.heading("NUM",text="NUM")
    treeview.heading("NAME",text="NAME")
    treeview.heading("BANLANCE",text="BANLANCE")
    treeview.heading("TYPE",text="TYPE")
    treeview.heading("PARA",text="PARA")
    treeview.heading("LOCATINO",text="LOCATINO")
    treeview.heading("NOTE",text="NOTE")
    treeview.place(x=20,y=10,anchor='nw')

    XL=20
    YL=250


    L1=tk.Label(window,text='  NUM').place(x=XL,y=YL)
    E1=tk.Entry(window)
    E1.place(x=XL+80,y=YL)

    L2=tk.Label(window,text='  NAME').place(x=XL,y=YL+40)
    E2=tk.Entry(window)
    E2.place(x=XL+80,y=YL+40)

    L3=tk.Label(window,text='BANLANCE').place(x=XL,y=YL+80)
    E3=tk.Entry(window)
    E3.place(x=XL+80,y=YL+80)

    L4=tk.Label(window,text='  TYPE').place(x=XL,y=YL+120)
    E4=tk.Entry(window)
    E4.place(x=XL+80,y=YL+120)

    L7=tk.Label(window,text='PARA').place(x=XL,y=YL+160)
    E7=tk.Entry(window)
    E7.place(x=XL+80,y=YL+160)

    L5=tk.Label(window,text='LOCATION').place(x=XL,y=YL+200)
    E5=tk.Entry(window)
    E5.place(x=XL+80,y=YL+200)

    L6=tk.Label(window,text='  NOTE').place(x=XL,y=YL+240)
    E6=tk.Entry(window)
    E6.place(x=XL+80,y=YL+240)

    XB=310
    YB=260
    B1=tk.Button(window,text='查询',width=12,height=1,command=find_num).place(x=XB,y=YB)
    B2=tk.Button(window,text='增加',width=12,height=1,command=Add).place(x=XB+100,y=YB)

    B4=tk.Button(window,text='刷新',width=12,height=1,command=getstu).place(x=XB,y=YB+160)

    B5=tk.Button(window,text='删除',width=12,height=1,command=delete).place(x=XB+100,y=YB+80)
    B4=tk.Button(window,text='修改',width=12,height=1,command=change).place(x=XB,y=YB+80)

    IN1=''
    IN2=''
    IN3=''
    IN4=''
    IN5=''
    IN6=''
    IN7=''

    getstu()
    treeview.bind("<Double-Button-1>",callback)
    
    window.mainloop

