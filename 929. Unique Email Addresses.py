# Runtime: 48 ms, faster than 83.81% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 14.4 MB, less than 62.51% of Python3 online submissions for Unique Email Addresses.

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            email = emails[i]

            local, domain = email.split('@')

            if '+' in email:
                local = local[:local.index('+')]

            local = local.replace('.','')

            emails[i] = local + '@' + domain

        return len(set(emails))
