#optionally you can define type hint of variable
var1:int=10

def function_name(par:int) -> str:
    return "something"


from typing import Any
var2:Any #variable can be any type, no type safety

#Generic type
var3:list[str]
var4:tuple[int, int, str]
var5:set[bytes]
var6:dict[str, float]
var7:int|str|None #value can be of int or str

#classes as types
class ClassName:
    pass
var8:ClassName #var8 is now a instance of ClassName class






