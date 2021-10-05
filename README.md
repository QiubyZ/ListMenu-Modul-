# Listmenu

```python

def A(): print("ini adalah def A")
def B(): print("ini adalah def B")
def C(): print("ini adalah def C")
def D(): print("ini adalah def D")
def E(args): print(f"ini adalah def {args}")

menu = MENU()
menu.add(func=A, info="Keterangan def A")
menu.add(func=B, info="Keterangan def B")
menu.add(func=C, info="Keterangan def C")
menu.add(func=D, info="Keterangan def D")
menu.add(func=E, args=('E'), info="Keterangan def parameter args")

menu.showListMenu()
while 1:
	a = menu.getFunctionNumber(int(input("Pilih Menu: ")))
	if(a != True):
		print("Menu yang dipilih tidak ada")

```
