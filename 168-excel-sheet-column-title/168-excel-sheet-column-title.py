class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        colnumnNum = 0
        excel_sheet = ""
        
        while columnNumber > 0:
            columnNum = columnNumber % 26
            
            if columnNum == 0:
                 columnNum = 26
                    
            excel_sheet = chr(64 + columnNum) + excel_sheet 
            
            if columnNumber % 26 == 0:
                columnNumber -= 1
                
            
            columnNumber = columnNumber // 26
        
        return excel_sheet