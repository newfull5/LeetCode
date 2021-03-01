class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        let = []

        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log)
            else:
                let.append(log)

        let = sorted(let, key = lambda x: x.split()[0])
        let = sorted(let, key = lambda x: x.split()[1:])

        return let+dig
