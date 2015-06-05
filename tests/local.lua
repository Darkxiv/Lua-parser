local a
b = "global"
c = {a = function (x, y) return x * y end}
c.a(2, 3)

function globalFunc1(x, y)
    local a, b, c = "local", "local", "local"
    d = "global"
    
    local function localFunc(x)
        return x
    end
    
    function globalFunc2(z)
        return z
    end
    
    function x.funcWithoutSelf(t)
        return t
    end
    
    function x:funcWithSelf(t)
        return t * self
    end
    
    for i = 1, 5 do  
        print(i)
    end
    
    while a do   -- repeat until GC
        print(a)
    end
end
