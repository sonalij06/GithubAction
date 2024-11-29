def compute_gate_output(gate, input1, input2):
    if gate == "AND":
        return [a & b for a, b in zip(input1, input2)]
    elif gate == "OR":
        return [a | b for a, b in zip(input1, input2)]
    elif gate == "NAND":
        return [~(a & b) & 1 for a, b in zip(input1, input2)]
    elif gate == "NOR":
        return [~(a | b) & 1 for a, b in zip(input1, input2)]
    elif gate == "XOR":
        return [a ^ b for a, b in zip(input1, input2)] 
    else:
        raise ValueError(f"Unsupported gate: {gate}")

def solve():
    N = int(input())
    gates = []
    for _ in range(N):
        line = input().strip()
        output, expression = line.split('=')
        output = output.strip()
        gate, inputs = expression.split('(')
        gate = gate.strip()
        inputs = inputs.strip(')').split(',')
        gates.append((output, gate, [inp.strip() for inp in inputs]))

    T = int(input())

    inputs = {}
    while True:
        line = input().strip()
        if len(line) == 1 and line.isalpha():
            required_gate = line
            break
        line = line.split()
        inputs[line[0]] = list(map(int, line[1:]))
    cycle = 0
    for i in gates:
        gate_name, gate_type, inputg = i
        if inputg[0] in inputs and inputg[0] in inputs:
            inputs[inputg[0]] = shift_array(inputs[inputg[0]])
            inputs[inputg[1]] = shift_array(inputs[inputg[1]])
            result = compute_gate_output(
                gate, inputs[inputg[0]], inputs[inputg[1]])
        if gate_name not in inputs:
            inputs[gate_name] = result
    print(" ".join(map(str, inputs[required_gate])))

def shift_array(arr):
    shifted_array = [0] + arr[:-1]  # Add 0 at the beginning and remove the last element
    return shifted_array
solve()
