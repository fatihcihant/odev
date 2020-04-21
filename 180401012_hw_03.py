# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:32:03 2020

@author: fatih cihan
"""


from sympy import Symbol,Piecewise
import sympy.plotting as syp
import matplotlib.pyplot as plt


"""
ÖDEV TANİMİ
Tekdüze dağılım (İngilizce:uniform distribution) olasılık kuramı ve istatistik bilim dallarında,
 her elemanı, olasılığın desteklendiği aynı büyüklükteki aralık içinde bulunabilir,
 her sürekli değer için aynı sabit olasılık gösteren bir olasılık dağılımları ailesidir. 
 Desteklenen aralık iki parametre ile, yani minimum değer a ve maksimum değer b ile, tanımlanmaktadır.
 Fatih Cihan Taşkın 180401012 
"""
a = Symbol('a')
b = Symbol('b')
x = Symbol('x')
f = 1 / abs(b-a)
def uniform_dist_syp(low_val, up_val):
    if low_val > up_val:#eger parametreler yanlis sirayla girilirse duzenlenecek
        low_val, up_val = up_val, low_val
    syp.plot(Piecewise((0, (x < low_val) | (x > up_val)), (f.subs({a:low_val , b:up_val,}), (x >= low_val) & (x <= up_val))), (x, -10, 10), title="uniform_distribution_sympy")
    
    
def uniform_dist_plt(low_val, up_val):
    if low_val > up_val:#eger parametreler yanlis sirayla girilirse duzenlenecek
        low_val, up_val = up_val, low_val
    x_value=[]
    y_value=[]
    function = Piecewise((0, (x < low_val) | (x > up_val)), (f.subs({a:low_val , b:up_val,}), (x >= low_val) & (x <= up_val)))
    """
    Fonksiyon tanimi:     f(x)=      |   1/(b-a)         a=<x=<b        |
                                     |    0          diger tum durumlar |
                                
    Piecewise: Bir dizi kosul ve karsilik gelen islevler verildiginde giris 
    verileri üzerindeki her bir işlevi, durumunun doğru olduğu yerlerde degerlendirir.Yani parcali fonksiyon yazma durumunu saglar.
    """    
    value = float(0)
    while value < 10.0:
        y=function.subs({x:value}).evalf()
        y_value.append(y)
        x_value.append(value)
        plt.title('uniform_distrbution_matplotlib')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.plot(x_value,y_value)
        value += 0.1#x degerlerinini bu sekilde az artirilmasi sebebi grafigi ideal konuma getirmeye calismaktir.

uniform_dist_syp(2,6)    #sayilar rastgele secilmistir
uniform_dist_plt(2,6)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    