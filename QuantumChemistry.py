import numpy as np

class QuantumChemistry:
    def __init__(self, E_elec_reactants, E_elec_products, E_elec_transition_state, 
                 frequencies_reactants, frequencies_products, frequencies_transition_state, 
                 temperature=298.15):
        """
        초기화 함수: 반응물, 생성물, 전이 상태의 전자 에너지 및 진동 모드를 입력받습니다.
        :param E_elec_reactants: 반응물의 전자 에너지 (J/mol)
        :param E_elec_products: 생성물의 전자 에너지 (J/mol)
        :param E_elec_transition_state: 전이 상태의 전자 에너지 (J/mol)
        :param frequencies_reactants: 반응물의 진동 모드 (cm^-1 단위의 리스트)
        :param frequencies_products: 생성물의 진동 모드 (cm^-1 단위의 리스트)
        :param frequencies_transition_state: 전이 상태의 진동 모드 (cm^-1 단위의 리스트)
        :param temperature: 계산 온도 (K), 기본값은 298.15K (실온)
        """
        self.R = 8.314  # 기체 상수 (J/(mol*K))
        self.k_B = 1.380649e-23  # 볼츠만 상수 (J/K)
        self.h = 6.62607015e-34  # 플랑크 상수 (J·s)
        self.c = 2.998e10  # 빛의 속도 (cm/s)
        self.T = temperature  # 절대 온도 (K)

        # 반응물, 생성물, 전이 상태의 에너지 및 진동 모드
        self.E_elec_reactants = E_elec_reactants
        self.E_elec_products = E_elec_products
        self.E_elec_transition_state = E_elec_transition_state

        self.frequencies_reactants = frequencies_reactants
        self.frequencies_products = frequencies_products
        self.frequencies_transition_state = frequencies_transition_state

    def calculate_zpe(self, frequencies):
        """
        영점 진동 에너지를 계산합니다 (ZPE).
        ZPE = 1/2 * Σ h * v_i
        여기서 v_i는 진동 모드의 주파수 (Hz)
        """
        zpe = 0.0
        for freq in frequencies:
            freq_in_hz = freq * self.c  # cm^-1를 Hz로 변환
            zpe += 0.5 * self.h * freq_in_hz
        zpe = zpe * 6.022e23  # J/mol로 변환
        return zpe

    def calculate_entropy(self, frequencies):
        """
        엔트로피 항(S)을 계산합니다.
        S = k_B * Σ (T * e^(-hv/kT))
        """
        S = 0.0
        for freq in frequencies:
            freq_in_hz = freq * self.c
            x = (self.h * freq_in_hz) / (self.k_B * self.T)
            S += (x / (np.exp(x) - 1)) - np.log(1 - np.exp(-x))
        S = self.R * S  # J/(mol*K) 단위로 변환
        return S

    def calculate_gibbs_free_energy(self, E_elec, frequencies):
        """
        기브스 자유 에너지를 계산합니다.
        G = E_elec + ZPE - TS
        """
        ZPE = self.calculate_zpe(frequencies)
        S = self.calculate_entropy(frequencies)
        G = E_elec + ZPE - (self.T * S)
        return G

    def calculate_equilibrium_constant(self, delta_G_reaction):
        """
        평형상수 계산: ΔG(reaction) = ΔG(products) - ΔG(reactants)
        평형상수: K = e^(-ΔG / RT)
        """
        K_eq = np.exp(-delta_G_reaction / (self.R * self.T))
        return K_eq

    def calculate_reaction_rate(self, delta_G_activation):
        """
        반응 속도 상수 계산 (전이 상태 이론):
        k = (k_B * T / h) * e^(-ΔG_activation / RT)
        """
        k_rate = (self.k_B * self.T / self.h) * np.exp(-delta_G_activation / (self.R * self.T))
        return k_rate

    def predict_reaction(self):
        """
        기브스 자유 에너지를 계산한 후, 평형상수와 반응 속도 상수를 이용하여 화학 반응을 예측하는 함수.
        """
        # 반응물, 생성물, 전이 상태의 기브스 자유 에너지 계산
        delta_G_reactants = self.calculate_gibbs_free_energy(self.E_elec_reactants, self.frequencies_reactants)
        delta_G_products = self.calculate_gibbs_free_energy(self.E_elec_products, self.frequencies_products)
        delta_G_transition_state = self.calculate_gibbs_free_energy(self.E_elec_transition_state, self.frequencies_transition_state)

        # 평형상수 계산
        delta_G_reaction = delta_G_products - delta_G_reactants
        K_eq = self.calculate_equilibrium_constant(delta_G_reaction)

        # 반응 속도 상수 계산
        delta_G_activation = delta_G_transition_state - delta_G_reactants
        k_rate = self.calculate_reaction_rate(delta_G_activation)

        # 결과 출력
        print(f"기브스 자유 에너지 (반응물): {delta_G_reactants:.3e} J/mol")
        print(f"기브스 자유 에너지 (생성물): {delta_G_products:.3e} J/mol")
        print(f"기브스 자유 에너지 (전이 상태): {delta_G_transition_state:.3e} J/mol")
        print(f"평형상수 (K_eq): {K_eq:.3e}")
        print(f"반응속도 상수 (k): {k_rate:.3e} s^-1")

        # 반응 경향성 및 속도 예측
        if K_eq > 1:
            print("반응이 생성물 쪽으로 진행됩니다.")
        else:
            print("반응이 반응물 쪽으로 진행됩니다.")

        if k_rate > 1e-3:
            print("반응이 빠르게 진행됩니다.")
        else:
            print("반응이 느리게 진행됩니다.")


# 예시 입력값: 전자 에너지 및 진동 모드 (단위: J/mol 및 cm^-1)
E_elec_reactants = -5.0e5  # 반응물의 전자 에너지
E_elec_products = -8.0e5   # 생성물의 전자 에너지
E_elec_transition_state = -4.0e5  # 전이 상태의 전자 에너지

frequencies_reactants = [500, 1000, 1500, 2000]  # 반응물의 진동 모드 (cm^-1)
frequencies_products = [600, 1100, 1600, 2100]   # 생성물의 진동 모드 (cm^-1)
frequencies_transition_state = [700, 1200, 1700, 2200]  # 전이 상태의 진동 모드 (cm^-1)

# QuantumChemistry 클래스 인스턴스 생성
qc = QuantumChemistry(E_elec_reactants, E_elec_products, E_elec_transition_state, 
                      frequencies_reactants, frequencies_products, frequencies_transition_state)

# 화학 반응 예측
qc.predict_reaction()
