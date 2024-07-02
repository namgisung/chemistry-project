import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_molecule(atoms, coordinates):
    # 원자 간 거리 계산
    def calculate_distance(coords1, coords2):
        return np.sqrt(np.sum((coords1 - coords2)**2))

    distances = []
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distances.append(calculate_distance(coordinates[i], coordinates[j]))

    print("원자 간 거리:")
    print(distances)

    # 간단한 에너지 계산
    bond_energies = {'C-H': 413, 'H-H': 436, 'O-H': 463, 'N-H': 391}
    total_energy = 0
    for distance in distances:
        if distance < 1.1:
            if atoms[0] == 'C':
                bond_type = 'C-H'
            elif atoms[0] == 'O':
                bond_type = 'O-H'
            elif atoms[0] == 'N':
                bond_type = 'N-H'
        else:
            bond_type = 'H-H'
        total_energy += bond_energies[bond_type]

    print("총 에너지:", total_energy, "kJ/mol")

    # 3D 플롯 생성
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 원자 위치 플롯
    ax.scatter(coordinates[:,0], coordinates[:,1], coordinates[:,2], c='r', marker='o')

    # 원자 라벨 표시
    for i, atom in enumerate(atoms):
        ax.text(coordinates[i,0], coordinates[i,1], coordinates[i,2], atom)

    # 결합선 추가
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distance = calculate_distance(coordinates[i], coordinates[j])
            if atoms[i] == 'C' and atoms[j] == 'C':
                bond_length = 1.54  # C-C 결합 길이
            elif (atoms[i] == 'C' and atoms[j] == 'H') or (atoms[i] == 'H' and atoms[j] == 'C'):
                bond_length = 1.09  # C-H 결합 길이
            elif atoms[i] == 'O' and atoms[j] == 'H':
                bond_length = 0.96  # O-H 결합 길이
            elif atoms[i] == 'N' and atoms[j] == 'H':
                bond_length = 1.01  # N-H 결합 길이
            else:
                continue  # 다른 경우는 무시

            if distance < bond_length * 1.2:  # 결합 길이의 120% 이내
                if atoms[i] == 'H' or atoms[j] == 'H':
                    # 수소 결합
                    ax.plot([coordinates[i,0], coordinates[j,0]], [coordinates[i,1], coordinates[j,1]], [coordinates[i,2], coordinates[j,2]], color='b', linestyle='--')
                else:
                    # 공유 결합
                    ax.plot([coordinates[i,0], coordinates[j,0]], [coordinates[i,1], coordinates[j,1]], [coordinates[i,2], coordinates[j,2]], color='black', linestyle='-')

    # 축 라벨 설정
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Molecule Structure')

    plt.show()

# 예시: 메탄 분자
atoms = ['C', 'H', 'H', 'H', 'H']
coordinates = np.array([[0.0, 0.0, 0.0], 
                       [0.63077, 0.63077, 0.63077],
                       [-0.63077, -0.63077, 0.63077],
                       [-0.63077, 0.63077, -0.63077],
                       [0.63077, -0.63077, -0.63077]])

plot_molecule(atoms, coordinates)

# 예시: 물 분자
atoms = ['O', 'H', 'H']
coordinates = np.array([[0.0, 0.0, 0.0],
                       [0.75735, 0.58310, 0.0],
                       [-0.75735, 0.58310, 0.0]])

plot_molecule(atoms, coordinates)

# 예시: 암모니아 분자
atoms = ['N', 'H', 'H', 'H']
coordinates = np.array([[0.0, 0.0, 0.0],
                       [0.93247, 0.0, 0.0],
                       [-0.46624, 0.80624, 0.0],
                       [-0.46624, -0.80624, 0.0]])

plot_molecule(atoms, coordinates)

# 예시: 이산화탄소 분자
atoms = ['C', 'O', 'O']
coordinates = np.array([[0.0, 0.0, 0.0],
                       [1.16, 0.0, 0.0],
                       [-1.16, 0.0, 0.0]])

plot_molecule(atoms, coordinates)

# 예시: 아세트산 분자
atoms = ['C', 'C', 'O', 'O', 'H', 'H', 'H', 'H']
coordinates = np.array([[0.0, 0.0, 0.0], 
                       [1.51, 0.0, 0.0],
                       [2.22, 1.15, 0.0],
                       [2.22, -1.15, 0.0],
                       [0.51, 0.88, 0.0],
                       [0.51, -0.88, 0.0],
                       [1.97, 1.89, 0.0],
                       [1.97, -1.89, 0.0]])

plot_molecule(atoms, coordinates)

# 예시: 에탄올 분자
atoms = ['C', 'C', 'O', 'H', 'H', 'H', 'H', 'H']
coordinates = np.array([[0.0, 0.0, 0.0],
                       [1.52, 0.0, 0.0],
                       [2.23, 1.22, 0.0],
                       [0.51, 0.89, 0.0],
                       [0.51, -0.89, 0.0],
                       [1.97, 1.99, 0.0],
                       [1.97, -1.99, 0.0],
                       [2.72, 0.63, 0.0]])

plot_molecule(atoms, coordinates)
