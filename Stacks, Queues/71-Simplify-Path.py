class Solution:
    def simplifyPath(self, path: str) -> str:
        dirOrFiles = []
        path = path.split(\/\)
        for elem in path:
            if dirOrFiles and elem == \..\:
                dirOrFiles.pop()
            elif elem not in [\.\, \\, \..\]:
                dirOrFiles.append(elem)
                
        return \/\ + \/\.join(dirOrFiles)