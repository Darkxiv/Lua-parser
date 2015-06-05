function action1()
 print("action1")
end

function action2(x, y)
 print("action2")
end

D = function (x) return x end
E = D(3)
D(3)
local T = function (x) return x end
T(3)
F = {bd=E}

function F.myget()
    return 42
end

print(F.myget())

G = 12
G["action"](F)
G["action"]:action(F)()
(2 + 2)[true] = 10
(2 + 2)"test"[true] = 10

local b = 10

function FSM(t)
  local function MYTEST(x) return x end
  local a = {}
  b = 10
  local c = {}
  glob = 10
  local loc = glob
  for _,v in ipairs(t) do
    local old, event, new, action = v[1], v[2], v[3], v[4]
    if a[old] == nil then a[old] = {} end
    a[old][event] = {new = new, action = action}
  end
  return a
end

fsm = FSM{
  {"state1", "event1", "state2", action1},
  {"state1", "event2", "state3", action2},
}


action2(E, F)
local a = fsm["state1"]["event1"]
state = a.new

