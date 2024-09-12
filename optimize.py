from scipy.optimize import minimize
import numpy as np


def optimize(rap, weights0, indices1, indices2, ub, lb, weights1, num_iterations):
    suggested_values = 0.5 * (ub + lb)

    # 目标函数，计算加权后的指标与建议值之间的绝对差值
    def objective(weights):
        weighted_indices = np.dot(weights[indices2.shape[0]-weights1.shape[0]:], indices1) + np.dot(weights[:indices2.shape[0]-weights1.shape[0]], indices2[:-weights1.shape[0], :]) + np.dot(weights1/100, indices2[indices2.shape[0]-weights1.shape[0]:, :])

        return np.sum(np.power(weighted_indices - suggested_values, 2))+np.sum(np.power(weights[indices2.shape[0]-weights1.shape[0]:] - weights0, 2))

    def inequality_constraint1(weights):
        # 将向量不等式条件转化为标量不等式条件
        inequality_values = np.dot(weights[indices2.shape[0]-weights1.shape[0]:], indices1) + np.dot(weights[:indices2.shape[0]-weights1.shape[0]], indices2[:-weights1.shape[0], :]) + np.dot(weights1/100, indices2[indices2.shape[0]-weights1.shape[0]:, :])
        return np.min(inequality_values - lb)

    def inequality_constraint2(weights):
        # 将向量不等式条件转化为标量不等式条件
        inequality_values =np.dot(weights[indices2.shape[0]-weights1.shape[0]:], indices1) + np.dot(weights[:indices2.shape[0]-weights1.shape[0]], indices2[:-weights1.shape[0], :]) + np.dot(weights1/100, indices2[indices2.shape[0]-weights1.shape[0]:, :])
        return np.min(ub - inequality_values)

    # 定义等式约束
    equality_constraint1 = {'type': 'eq', 'fun': lambda weights: np.sum(weights[:indices2.shape[0]-weights1.shape[0]]) -(1- rap/100 - np.sum(weights1)/100)}
    equality_constraint2 = {'type': 'eq', 'fun': lambda weights: np.sum(weights[indices2.shape[0]-weights1.shape[0]:]) - rap / 100}

    # 定义权重的界限，每个权重在0和1之间
    if weights1.shape[0] + indices2.shape[0] == 0:
        best_result = 0
    else:
        bounds = [(0, 1) for _ in range(indices2[:-weights1.shape[0], :].shape[0]+weights0.shape[0])]
        best_result = None
        for _ in range(num_iterations):
            initial_guess = np.random.rand(indices2[:-weights1.shape[0], :].shape[0])  # 生成随机的初始猜测权重
            guess = np.concatenate((initial_guess, weights0))
            result = minimize(
                objective,
                guess,
                method='SLSQP',
                bounds=bounds,
                constraints=[equality_constraint1,equality_constraint2, {'type': 'ineq', 'fun': inequality_constraint1},
                             {'type': 'ineq', 'fun': inequality_constraint2}],
            )
            if best_result is None or result.fun < best_result.fun:
                best_result = result
    if best_result != 0:
        print(best_result.x)
    return best_result
