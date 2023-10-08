from typing import Any


class State:
    # Khởi tạo lớp State với các thuộc tính Monk, Ghost và Edge
    def __init__(self, Monk = 3, Ghost = 3, Edge = 'A'):
        self.Monk = Monk # Số lượng nhà sư
        self.Ghost = Ghost # Số lượng hồn ma
        self.Edge = Edge # Bờ hiện tại

    # Phương thức di chuyển 1 nhà sư
    def Move_1_Monk(self, Result):
        if self.Edge=='A' and self.Monk>0: # Nếu đang ở bờ A và có ít nhất 1 nhà sư
            Result.Monk = self.Monk - 1 # Giảm số lượng nhà sư đi 1
            Result.Ghost = self.Ghost # Số lượng hồn ma không đổi
            Result.Edge = 'B' # Chuyển sang bờ B
            return Result
        elif self.Edge=='B' and self.Monk<3: # Nếu đang ở bờ B và có ít hơn 3 nhà sư
            Result.Monk = self.Monk+1 # Tăng số lượng nhà sư lên 1
            Result.Ghost = self.Ghost # Số lượng hồn ma không đổi
            Result.Edge = 'A' # Chuyển sang bờ A
            return Result
        return None

    # Phương thức di chuyển 2 nhà sư
    def Move_2_Monks(self, Result):
        if self.Edge=='A' and self.Monk>1: # Nếu đang ở bờ A và có ít nhất 2 nhà sư
            Result.Monk = self.Monk - 2 # Giảm số lượng nhà sư đi 2
            Result.Ghost = self.Ghost # Số lượng hồn ma không đổi
            Result.Edge = 'B' # Chuyển sang bờ B
            return Result
        elif self.Edge=='B' and self.Monk<2: # Nếu đang ở bờ B và có ít hơn 2 nhà sư
            Result.Monk = self.Monk + 2 # Tăng số lượng nhà sư lên 2
            Result.Ghost = self.Ghost # Số lượng hồn ma không đổi
            Result.Edge = 'A' # Chuyển sang bờ A
            return Result
        return None

    # Phương thức di chuyển 1 hồn ma
    def Move_1_Ghost(self, Result):
        if self.Edge=='A' and self.Ghost>0: # Nếu đang ở bờ A và có ít nhất 1 hồn ma
            Result.Ghost = self.Ghost - 1 # Giảm số lượng hồn ma đi 1
            Result.Monk = self.Monk # Số lượng nhà sư không đổi
            Result.Edge = 'B' # Chuyển sang bờ B
            return Result
        elif self.Edge=='B' and self.Ghost<3: # Nếu đang ở bờ B và có ít hơn 3 hồn ma
            Result.Ghost = self.Ghost + 1 # Tăng số lượng hồn ma lên 1
            Result.Monk = self.Monk # Số lượng nhà sư không đổi
            Result.Edge = 'A' # Chuyển sang bờ A
            return Result
        return None

    # Phương thức di chuyển 2 hồn ma
    def Move_2_Ghosts(self, Result):
        if self.Edge=='A' and self.Ghost>1: # Nếu đang ở bờ A và có ít nhất 2 hồn ma
            Result.Ghost = self.Ghost - 2 # Giảm số lượng hồn ma đi 2
            Result.Monk = self.Monk # Số lượng nhà sư không đổi
            Result.Edge = 'B' # Chuyển sang bờ B
            return Result
        elif self.Edge=='B' and self.Ghost<2: # Nếu đang ở bờ B và có ít hơn 2 hồn ma
            Result.Ghost = self.Ghost + 2 # Tăng số lượng hồn ma lên 2
            Result.Monk = self.Monk # Số lượng nhà sư không đổi
            Result.Edge = 'A' # Chuyển sang bờ A
            return Result
        return None

    # Phương thức di chuyển 1 nhà sư và 1 hồn ma
    def Move_1_Each_Kind(self, Result):
        if self.Edge=='A' and self.Monk>0 and self.Ghost>0: # Nếu đang ở bờ A và có ít nhất 1 nhà sư và 1 hồn ma
            Result.Monk = self.Monk - 1 # Giảm số lượng nhà sư đi 1
            Result.Ghost = self.Ghost - 1 # Giảm số lượng hồn ma đi 1
            Result.Edge = 'B' # Chuyển sang bờ B
            return Result
        elif self.Edge=='B' and self.Monk<3 and self.Ghost<3: # Nếu đang ở bờ B và có ít hơn 3 nhà sư và ít hơn 3 hồn ma
            Result.Monk = self.Monk + 1 # Tăng số lượng nhà sư lên 1
            Result.Ghost = self.Ghost + 1 # Tăng số lượng hồn ma lên 1
            Result.Edge = 'A' # Chuyển sang bờ A
            return Result
        return None

    # Phương thức gọi các phương thức di chuyển khác nhau dựa trên giá trị của Option
    def Call(self, Result, Option):
        if Option == 1:
            return self.Move_1_Monk(Result)
        elif Option == 2:
            return self.Move_2_Monks(Result)
        elif Option == 3:
            return self.Move_1_Ghost(Result)
        elif Option == 4:
            return self.Move_2_Ghosts(Result)
        elif Option == 5:
            return self.Move_1_Each_Kind(Result)
        else:
            return None

    # Phương thức kiểm tra trạng thái hiện tại có hợp lệ hay không
    def Valid_State(self):
        if self.Edge=='A' and self.Ghost > self.Monk and self.Monk != 0: # Nếu đang ở bờ A và số lượng hồn ma nhiều hơn số lượng nhà sư và có ít nhất một nhà sư
            return False
        if self.Edge=='A' and self.Ghost < self.Monk and self.Monk != 3: # Nếu đang ở bờ A và số lượng hồn ma ít hơn số lượng nhà sư và có ít hơn ba nhà sư
            return False
        if self.Edge=='B' and self.Ghost > self.Monk and self.Monk != 0: # Nếu đang ở bờ B và số lượng hồn ma nhiều hơn số lượng nhà sư và có ít nhất một nhà sư
            return False
        if self.Edge=='B' and self.Ghost < self.Monk and self.Monk != 3: # Nếu đang ở bờ B và số lượng hồn ma ít hơn số lượng nhà sư và có ít hơn ba nhà sư
            return False
        return True

    # Phương thức kiểm tra xem đã đạt được mục tiêu hay chưa (tất cả các nhà sư và hồn ma đã chuyển sang bờ B)
    def Is_Goal(self):
        return self.Ghost==0 and self.Monk==0 and self.Edge=='B'

    # Phương thức in ra trạng thái hiện tại của các thuộc tính Monk, Ghost và Edge
    def Print_State(self):
        print("Nhà sư:",self.Monk,"| Hồn ma:",self.Ghost,"| Bờ:",self.Edge)

class Node:
    # Khởi tạo lớp Node với các thuộc tính State, Dad và Order
    def __init__(self, State, Dad = None, Order = 0):
        self.State = State # Trạng thái hiện tại
        self.Dad = Dad # Trạng thái trước đó
        self.Order = Order # Thứ tự hành động

# Hàm so sánh hai trạng thái S1 và S2 có giống nhau hay không
def Compare_States(S1, S2):
    return S1.Edge==S2.Edge and S1.Monk==S2.Monk and S1.Ghost==S2.Ghost

# Hàm tìm kiếm trạng thái S trong danh sách List
def Find_State(S, List):
    for Item in List:
        if Compare_States(Item.State, S): # Nếu trạng thái Item.State giống với trạng thái S
            return True
    return False

# Danh sách các hành động có thể thực hiện
Action = ["First state","Move one monk","Move two monks","Move one ghost","Move two ghosts","Move one each kind"]

# Hàm lấy đường đi từ trạng thái ban đầu đến trạng thái mục tiêu
def Get_Path(Goal):
    List = []
    while Goal.Dad != None: # Lặp cho đến khi trạng thái trước đó của Goal là None (trạng thái ban đầu)
        List.append(Goal) # Thêm Goal vào danh sách List
        Goal = Goal.Dad # Cập nhật Goal bằng trạng thái trước đó của nó
    List.append(Goal) # Thêm trạng thái ban đầu vào danh sách List
    List.reverse() # Đảo ngược danh sách List để có được đường đi từ trạng thái ban đầu đến trạng thái mục tiêu
    Order = 0
    for Item in List:
        print("Action:",Order,Action[Item.Order]) # In ra hành động tại bước Order
        Item.State.Print_State() # In ra trạng thái sau khi thực hiện hành động
        Order+=1

# Hàm tìm kiếm theo chiều sâu (Depth-First Search)
def DFS(First_State):
    IsOpen = [] # Danh sách các trạng thái chưa xét (Open list)
    Closed = [] # Danh sách các trạng thái đã xét (Closed list)
    Root = Node(First_State) # Khởi tạo nút gốc với trạng thái ban đầu First_State
    IsOpen.append(Root) # Thêm nút gốc vào Open list
    while len(IsOpen) != 0: # Lặp cho đến khi Open list rỗng
        Top = IsOpen.pop(0) # Lấy ra phần tử đầu tiên của Open list và xóa nó khỏi Open list
        Closed.append(Top) # Thêm phần tử vừa lấy ra vào Closed list
        if Top.State.Is_Goal(): # Nếu phần tử vừa lấy ra là trạng thái mục tiêu
            Get_Path(Top) # Lấy và in ra đường đi từ trạng thái ban đầu đến trạng thái mục tiêu
            return
        for Option in range(1,5+1,1): # Duyệt qua các hành động có thể thực hiện (từ 1 đến 5)
            Child_State = State()
            Child_State = Top.State.Call(Child_State,Option) # Tạo ra trạng thái mới sau khi thực hiện hành động Option từ trạng thái Top.State
            if Child_State != None: # Nếu trạng thái mới hợp lệ
                Existed_IsOpen = Find_State(Child_State,IsOpen) # Kiểm tra xem trạng thái mới có tồn tại trong Open list hay không
                Existed_Closed = Find_State(Child_State,Closed) # Kiểm tra xem trạng thái mới có tồn tại trong Closed list hay không
                if not Existed_IsOpen and not Existed_Closed and Child_State.Valid_State(): # Nếu trạng thái mới không tồn tại trong cả hai danh sách và là trạng thái hợp lệ
                    Child_Node = Node(Child_State, Top, Option) # Tạo nút mới với trạng thái là Child_State, trạng thái trước đó là Top và hành động thực hiện là Option
                    IsOpen.insert(0,Child_Node) # Thêm nút mới vào đầu Open list
    return None

DFS(State()) # Gọi hàm DFS với trạng thái ban đầu là State()