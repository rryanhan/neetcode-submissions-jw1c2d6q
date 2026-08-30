class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        counter = 0

        q.append("0000")
        visited = set(deadends)

        while q:
            
            for _ in range(len(q)):
                password = q.popleft()
                if password == target:
                    return counter
                if password in visited:
                    continue
                visited.add(password)

                for i in range(len(password)):
                    digits_forward = list(password)
                    num_forward = int(digits_forward[i])
                    forward = (num_forward + 1) % 10
                    digits_forward[i] = str(forward)
                    forward_password = "".join(digits_forward)
                    q.append(forward_password)

                    digits_backward = list(password)
                    num_backward = int(digits_backward[i])
                    backward = (num_backward - 1 + 10) % 10
                    digits_backward[i] = str(backward)
                    backward_password = "".join(digits_backward)
                    q.append(backward_password)

            counter += 1
        return -1
                
            

        