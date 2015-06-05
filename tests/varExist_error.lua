a = 10
b = c
b = a
e.a = 10

function globalFunc(x, y)
    local function localFunc(x)
        return y
    end
    
    local c = 10
    localFunc(d)
    
    for x in d do
        print(x)
    end
end

b = c
globalFunc(a, b)
localFunc(b)
noFunc()
