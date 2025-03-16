def solution(num_list):
    def count_operations(n):
        count = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = (n - 1) // 2
            count += 1
        return count

    total_operations = sum(count_operations(num) for num in num_list)
    
    return total_operations