a = 10
b = a

function globalFunc(x, y)
    local function localFunc(x)
        return x
    end
    
    local c = 10
    localFunc(c)
    localFunc(a)
    
    for x in b do
        print(x)
    end
end

globalFunc(a, b)
