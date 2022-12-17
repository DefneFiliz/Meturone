class Blocks:

    def __init__(self, cornerList):

        self.cornerList = cornerList

        if cornerList[0] < cornerList[2] and cornerList[1] < cornerList[3]:
            lowerLeft = [cornerList[0], cornerList[1]]
            lowerRight = [cornerList[2], cornerList[1]]
            upperLeft = [cornerList[0], cornerList[3]]
            upperRight = [cornerList[2], cornerList[3]]

        elif cornerList[0] < cornerList[2] and cornerList[1] > cornerList[3]:
            lowerLeft = [cornerList[0], cornerList[3]]
            lowerRight = [cornerList[2], cornerList[3]]
            upperLeft = [cornerList[0], cornerList[1]]
            upperRight = [cornerList[2], cornerList[1]]

        elif cornerList[0] > cornerList[2] and cornerList[1] < cornerList[3]:
            lowerLeft = [cornerList[2], cornerList[1]]
            lowerRight = [cornerList[0], cornerList[1]]
            upperLeft = [cornerList[2], cornerList[3]]
            upperRight = [cornerList[0], cornerList[3]]
        
        elif cornerList[0] > cornerList[2] and cornerList[1] > cornerList[3]:
            lowerLeft = [cornerList[2], cornerList[3]]
            lowerRight = [cornerList[0], cornerList[3]]
            upperLeft = [cornerList[2], cornerList[1]]
            upperRight = [cornerList[0], cornerList[1]]

        self.lowerLeft = lowerLeft
        self.lowerRight = lowerRight
        self.upperLeft = upperLeft
        self.upperRight = upperRight

    
    def area(self):
        x = self.lowerRight[0] - self.lowerLeft[0]
        y = self.upperLeft[1] - self.lowerLeft[1]
        return x * y


    def centerOfMass(self):
        x = (self.upperLeft[0] + self.upperRight[0]) / 2
        y = (self.upperLeft[1] + self.lowerLeft[1]) / 2
        return [x, y]


def overlap(b1, b2):
    x = min(b1.upperRight[0], b2.upperRight[0]) - max(b1.upperLeft[0], b2.upperLeft[0])
    y = min(b1.upperRight[1], b2.upperRight[1]) - max(b1.lowerRight[1], b2.lowerRight[1])
    if x < 0 or y < 0:
        return 0
    else:
        return x * y



def is_firmus(cornerList1, cornerList2):
    
    block1 = Blocks(cornerList1)
    block2 = Blocks(cornerList2)

    if block1.centerOfMass()[1] < block2.centerOfMass()[1]:
        upper = block2
        lower = block1 
    
    elif block1.centerOfMass()[1] > block2.centerOfMass()[1]:
        upper = block1
        lower = block2 

    else:
        totalArea = block1.area() + block2.area() - overlap(block1, block2)
        return ["DAMNARE", totalArea]

    #I
    if lower.lowerLeft[1] != 0 and lower.lowerRight[1] != 0:
        totalArea = upper.area() + lower.area() - overlap(upper, lower)
        return ["DAMNARE", totalArea]

    else:
    #II
        if lower.upperLeft[1] != upper.lowerLeft[1]:
            totalArea = upper.area() + lower.area() - overlap(upper, lower)
            return ["DAMNARE", totalArea]        

        else:
            
            if upper.lowerLeft[0] >= lower.upperRight[0]:
                totalArea = upper.area() + lower.area() - overlap(upper, lower)
                return ["DAMNARE", totalArea]
            
            elif upper.lowerRight[0] <= lower.upperLeft[0]:
                totalArea = upper.area() + lower.area() - overlap(upper, lower)
                return ["DAMNARE", totalArea]

            else:
                #III
                if lower.upperLeft[0] < upper.centerOfMass()[0] < lower.upperRight[0]:
                    totalArea = upper.area() + lower.area()
                    return ["FIRMUS", totalArea]

                else:
                    if upper.centerOfMass()[0] < lower.upperLeft[0]:
                        distance = lower.upperLeft[0] - upper.centerOfMass()[0]
                        x1 = upper.lowerRight[0]
                        y1 = upper.lowerRight[1]
                        x2 = upper.upperRight[0] + distance*2
                        y2 = upper.upperRight[1]
            
                    else:
                        distance = upper.centerOfMass()[0] - lower.upperRight[0]
                        x1 = upper.lowerLeft[0]
                        y1 = upper.lowerLeft[1]
                        x2 = upper.upperLeft[0] - distance*2
                        y2 = upper.upperLeft[1]

                    return ["ADDENDUM", [x1, y1, x2, y2]]
             
                
                    

test = is_firmus([-8,11,2,5],[1,0,-2,5])
print(test)
                    



    
        

            
               





                



        
            

       



        

        


    
       

   
        
                

        

