class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        allEmails = set()
        for email in emails:
            curr = email.split("@")[0]
            domainName = email.split("@")[1]
            nextWord = curr
            if "." in curr:
                nextWord = "".join(curr.split("."))
            if "+" in curr:
                nextWord = (nextWord.split("+")[0])
            allEmails.add(nextWord+"@"+domainName)
        return len(allEmails)
            
