local a
b = "global"
e.a = 10
f.a()
g:a()
g.a:a()

function globalFunc1(x, y)
    local a, b, c = "local", "local", "local"
    
    local function localFunc(x)
        return x
    end
    
    function globalFunc2(z)
        return z
    end
    
    function k:funcWithSelf(t)
        return t * self
    end
    
    for i = 1, 5 do  
        print(i)
    end
    
    while a do   -- repeat until GC
        print(a)
    end
end
