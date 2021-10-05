# Listmenu

```python

def A(): print("ini adalah def A")
def B(): print("def B")
def C(): print("def C")
def D(): print("def D")

menu = MENU()
menu.add(func=A, info="Keterangan def A")
menu.add(func=B, info="Keterangan def B")
menu.add(func=C, info="Keterangan def C")
menu.add(func=D, info="Keterangan def D")

menu.showListMenu()
while 1:
	menu.getFunctionNumber(int(input("Pilih Menu: ")))

```
