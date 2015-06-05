f.a()
g:a()
g.a:a()

function globalFunc(x, y)
    local function localFunc(x)
        return x
    end
    
    local a, b = "a", "b"
    localFunc(a)
    localFunc(a, b)
    localFunc()
    
    localFunc():test()
    localFunc().test()
    
    return x * y
end

local a, b, c = "a", "b", "c"

globalFunc(a, b)
globalFunc(a, b, c)
globalFunc(a)
