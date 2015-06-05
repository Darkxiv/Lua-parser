a = 10
b = a

function globalFunc(x, y)
    local function localFunc(x)
        return x
    end
    
    local c = 10
    localFunc(c)
    localFunc(a)
    localFunc(a).test()
    localFunc(a):test()
    
    for x in b do
        print(x)
    end
end

globalFunc(a, b)
