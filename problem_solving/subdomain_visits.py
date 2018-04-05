class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        map = {}
        for domain in cpdomains:
            count, *domains_arr = domain.replace(" ",".").split(".")
            for i in range(len(domains_arr)):
                item = ".".join(domains_arr[i:])
                if not item in map: 
                    map[item] = int(count)
                else: 
                    map[item] += int(count)
        return [" ".join((str(v), k)) for k, v in map.items()]