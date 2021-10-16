function step(p::Array{Int64,1},v::Array{Int64,1})
    for i in 1:4
        v[i] += sum([(p[i] < p[j]) for j in 1:4])
        v[i] -= sum([(p[i] > p[j]) for j in 1:4])
    end
    p += v
    return p, v
end

function period(p::Array{Int64,1},v::Array{Int64,1})
    periods = Int64[0, 0, 0, 0]
    done = Int8[0, 0, 0, 0]
    p_0, v_0 = copy(p), copy(v)
    n = 0
    while true
        p, v = step(p, v)
        n += 1
        done = ((p == p_0) && (v == v_0))
        if done
            return n
        end
    end
end

function gcd(x::Int,y::Int)
    return x/numerator(x//y)
end

function solve(p::Array{Int64,2},v::Array{Int64,2})
    periods = Int64[]
    for i in 1:3
        push!(periods, period(p[:,i],v[:,i]))
    end
    return reduce((x,y) -> convert(Int,x*y/gcd(x,y)),periods)
end

filepath = "C:/Users/lando/Desktop/Python/Advent of Code 2019/Day 12/Part 2/input.txt"
p = open(filepath) do file
    lines = readlines(file)
    p = Int64[]
    for line in lines
        line = replace(replace(line,">" => ""),"<" => "")
        vars = split(line,", ")
        for var in vars
            eval(Meta.parse(var))
        end
        if length(p) == 0
            p = [x y z]
        else
            p = [p; x y z]
        end
    end
    return p
end

v = [0 0 0
     0 0 0
     0 0 0
     0 0 0]

answer = solve(p,v)
println(answer)