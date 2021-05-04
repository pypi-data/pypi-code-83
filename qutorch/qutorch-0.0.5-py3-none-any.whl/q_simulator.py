import torch
from torch.utils.data.sampler import WeightedRandomSampler
from collections import Counter, OrderedDict
import numpy as np
import math  
import pandas as pd
import itertools

# We define the elemental quantum gates

#Hadamard
H_t = torch.tensor([
[1/np.sqrt(2), 1/np.sqrt(2)],
[1/np.sqrt(2), -1/np.sqrt(2)]
],  dtype=torch.cfloat)

#Pauli-X
X_t = torch.tensor([
[0, 1],
[1, 0]
],  dtype=torch.cfloat)

#Pauli-Y
Y_t = torch.tensor([
[0, -1j],
[1j, 0]
],  dtype=torch.cfloat)

#Pauli-Z
Z_t = torch.tensor([
[1, 0],
[0, -1]
],  dtype=torch.cfloat)

#Sd
SD_t = torch.tensor([
[1, 0],
[0, 0-1j]
],  dtype=torch.cfloat)

#Swap gate
Swap_t = torch.tensor([
[1, 0, 0, 0],
[0, 0, 1, 0],
[0, 1, 0, 0],
[0, 0, 0, 1]
],  dtype=torch.cfloat)

#Projector in 0
P0x0_t = torch.tensor([
[1, 0],
[0, 0]
],  dtype=torch.cfloat)

#Projector in 1
P1x1_t = torch.tensor([
[0, 0],
[0, 1]
],  dtype=torch.cfloat)

def kron(a, b):
    #return the kronecker product between two tensors
    assert a.dim() == b.dim()
    a_view_shape = []
    b_view_shape = []
    ab_view_shape = []
    for i in range(a.dim()):
        a_view_shape.append(a.size(i))
        a_view_shape.append(1)
        b_view_shape.append(1)
        b_view_shape.append(b.size(i))
        ab_view_shape.append(a.size(i) * b.size(i))
    return (a.reshape(a_view_shape) * 
            b.reshape(b_view_shape)).reshape(ab_view_shape)

def get_ground_state(num_qubits):
    # return vector of size 2**num_qubits with all zeroes except first element which is 1
    state = torch.zeros(1, 2**num_qubits, dtype=torch.cfloat).t()
    state[0,0] =  1+0j
    return state

def get_dqc1_ground_state(ensemble_qubits):
    state = torch.zeros(1, 2, dtype=torch.cfloat).t()
    state[0,0] =  1+0j
    state = torch.matmul(state, state.conj().t())

    identity = torch.eye(2**(ensemble_qubits))
    state = kron(state, identity)

    return state/2**(ensemble_qubits)

def formulate_u3(parameters):
    #return the matrix definition of the u3 gate given theta, phi and lambda 
    theta = float(parameters["theta"])
    phi = float(parameters["phi"])
    lam = float(parameters["lambda"])

    cos = np.cos(theta / 2)
    sin = np.sin(theta / 2)

    u3 = torch.tensor([
    [cos, -np.exp(1j * lam) * sin],
    [np.exp(1j * phi) * sin, np.exp(1j * (phi + lam)) * cos]
    ],  dtype=torch.cfloat)

    return u3

def formulate_rx(angle):
    angle = float(angle)

    cos = np.cos(angle/2)
    sin = np.sin(angle/2)

    rx = torch.tensor([
                       [cos, -1j*sin],
                       [-1j*sin, cos]
                       ], 
                      dtype=torch.cfloat
                      )
    
    return rx

def formulate_ry(angle):
    angle = float(angle)

    cos = np.cos(angle/2)
    sin = np.sin(angle/2)

    ry = torch.tensor([
                       [cos, -sin],
                       [sin, cos]
                       ], 
                      dtype=torch.cfloat
                      )
    
    return ry

def formulate_rz(angle):
    angle = float(angle)

    rz = torch.tensor([
                       [np.exp(-1j * angle/2), 0],
                       [0, np.exp(1j * angle/2)]
                       ], 
                      dtype=torch.cfloat)
            
    return rz

def get_operator(total_qubits,
                 gate_unitary, 
                 target_qubits, 
                 cuda = False):
  
    # return unitary operator of given gate and target qubits

    identity = torch.eye(2).cuda() if cuda else torch.eye(2)
    gate_unitary = gate_unitary.cuda() if cuda else gate_unitary

    if target_qubits[0] == 0:
        current_gate = gate_unitary
    else:
        current_gate = identity

    for i in range(1, total_qubits):
        if i in target_qubits:
            current_gate = kron(current_gate, gate_unitary)
        else:
            current_gate = kron(current_gate, identity)

    return current_gate

def to_gate(program, number_of_qubits, cuda = False):
    
    initial_gate = compute_instruction(program.pop(0), number_of_qubits, cuda) 
    initial_gate = initial_gate.cuda() if cuda else initial_gate
    number_of_qubits = initial_gate.shape[1].bit_length() - 1

    for instruction in program:
        current_operator = compute_instruction(instruction, number_of_qubits, cuda)
        initial_gate = torch.matmul(initial_gate, current_operator)

    return initial_gate

def run_program(initial_state, program, params = None, cuda = False):
    
    # read program, and for each gate:
    #   - calculate matrix operator
    #   - multiply state with operator
    # return final state

    initial_state = initial_state.cuda() if cuda else initial_state
    number_of_qubits = initial_state.shape[1].bit_length() - 1
    for instruction in program:
        current_operator = compute_instruction(instruction, number_of_qubits, params, cuda)
        initial_state =  torch.matmul(torch.matmul(current_operator, initial_state), current_operator.conj().t() )

    return initial_state

def compute_instruction(instruction, number_of_qubits, params = None, cuda = False):
    
    if instruction["gate"]  == "h":
        current_operator = get_operator(number_of_qubits, H_t, 
                                        instruction["target"],
                                        cuda = cuda)
    elif instruction["gate"]  == "x":
        current_operator = get_operator(number_of_qubits, X_t,
                                        instruction["target"],
                                        cuda = cuda)
    elif instruction["gate"]  == "z":
        current_operator = get_operator(number_of_qubits, Z_t,
                                        instruction["target"],
                                        cuda = cuda)
    elif instruction["gate"]  == "sd":
        current_operator = get_operator(number_of_qubits, SD_t,
                                        instruction["target"],
                                        cuda = cuda)
    elif instruction["gate"]  == "y":
        current_operator = get_operator(number_of_qubits, Y_t,
                                        instruction["target"],
                                        cuda = cuda)
    elif instruction["gate"]  == "u3":
        current_gate = formulate_u3(instruction["params"] if params is None else params)
        current_operator = get_operator(number_of_qubits, current_gate,
                                        instruction["target"],
                                        cuda = cuda)
    elif instruction["gate"]  == "cx":
        current_operator = get_controlled_operator(number_of_qubits, X_t,
                                                    instruction["control"],  
                                                    instruction["target"],
                                                    cuda = cuda)   
    elif instruction["gate"]  == "cng":
        current_operator = get_controlled_operator(number_of_qubits, instruction["custom_gate"],
                                                    instruction["control"],  
                                                    instruction["target"],
                                                    cuda = cuda)
    elif instruction["gate"] == "cu3":
        current_gate = formulate_u3(instruction["params"] if params is None else params)
        current_operator = get_controlled_operator(number_of_qubits, current_gate,
                                                    instruction["control"],  
                                                    instruction["target"],
                                                    cuda = cuda) 
    elif instruction["gate"] == "rx":
        current_gate = formulate_rx(instruction["params"])
        current_operator = get_operator(number_of_qubits,
                                        current_gate,
                                        instruction["target"],
                                        cuda=cuda)
    elif instruction["gate"] == "ry":
        current_gate = formulate_ry(instruction["params"])
        current_operator = get_operator(number_of_qubits,
                                        current_gate,
                                        instruction["target"],
                                        cuda=cuda)
    elif instruction["gate"] == "rz":
        current_gate = formulate_rz(instruction["params"])
        current_operator = get_operator(number_of_qubits,
                                        current_gate,
                                        instruction["target"],
                                        cuda=cuda)
    return current_operator

def get_normalized_trace(density_matrix, target, cuda = False):
    #print(density_matrix)
    number_of_qubits = density_matrix.shape[1].bit_length() - 1
    pauli_x_m = get_operator(number_of_qubits, X_t,
                                  target,
                                  cuda = cuda)
    pauli_y_m = get_operator(number_of_qubits, Y_t,
                              target,
                              cuda = cuda) 

    x_exp =  torch.matmul(density_matrix, pauli_x_m)
    y_exp =  torch.matmul(density_matrix, pauli_y_m)

    real, img = torch.trace(x_exp), torch.trace(y_exp)
    #print(real)
    #print(img)

    if cuda:
        real, img = real.cpu().data.numpy(), img.cpu().data.numpy()
    else:
        real, img = real.data.numpy(), img.data.numpy()

    return real.real, img.real

def get_counts(density_matrix, num_shots, target, print_results = False):

    dm_diag = torch.diagonal(density_matrix, 0)
    special_qubit = torch.diagonal(density_matrix, 0)[len(dm_diag) //2 - 1: len(dm_diag) // 2 + 1]

    number_of_qubits = density_matrix.shape[1].bit_length() - 1
    sampler = WeightedRandomSampler(special_qubit, num_shots)
    format = '{0:0' + str(density_matrix.shape[1].bit_length() - 1) + 'b}'

    counter = Counter() 
    for idx in sampler:
        counter[idx] += 1

    counter_s = sorted(counter.items())
    # m_counts = counter_s[0][1] - counter_s[1][1]
    m_counts = counter[0] - counter[1]

    return  m_counts / num_shots

    if print_results:
        print('{')
        for element in sorted(counter.items()) :
            print("\t\"" +  format.format(element[0]) + '\" : ' + str(element[1]))
        print('}')

    return counter

def get_controlled_operator(total_qubits, 
                            gate_unitary,
                            control_qubits,
                            target_qubits, 
                            cuda = False):
  
    # return controlled unitary operator given gate and target qubits

    identity = torch.eye(2).cuda() if cuda else torch.eye(2)
    gate_unitary = gate_unitary.cuda() if cuda else gate_unitary
    p_a = [P0x0_t.cuda() if cuda else P0x0_t, P1x1_t.cuda() if cuda else P1x1_t]
    
    current_gates = [None] * 2 ** len(control_qubits)
    bin_nums = [list(i) for i in itertools.product([0, 1], repeat=len(control_qubits))]
    i = 0

    for i, projection in enumerate(bin_nums):
        j, k = 0, 0
        while current_gates[i] is None or current_gates[i].shape[0] < 2 ** total_qubits:
              if k in control_qubits:
                  current_gates[i] =  kron(current_gates[i] , p_a[projection[j]]) if current_gates[i] is not None else p_a[projection[j]]
                  j+= 1
              elif k in target_qubits and all(projection):
                  current_gates[i] =  kron(current_gates[i] , gate_unitary) if current_gates[i] is not None else gate_unitary
              else:
                  current_gates[i] =  kron(current_gates[i] , identity) if current_gates[i] is not None else identity

              k += 1

    return sum(current_gates)