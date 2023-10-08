#include<stdio.h>
#include<stdlib.h>
#include<stack>
using namespace std;
struct State{
    int Monk, Ghost;
    char Edge;

};
void Makenullstate(State *State){
    State->Monk = 3;
    State->Ghost = 3;
    State->Edge = 'A';
}
struct Node{
    State State;
    Node *P;
    int Order;
};
int Move_1_Monk(State Current, State *Result){
    if(Current.Edge=='A'&&Current.Monk>0){
        Result->Monk = Current.Monk - 1;
        Result->Ghost = Current.Ghost;
        Result->Edge = 'B';
        return 1;
    }else if(Current.Edge=='B'&&Current.Monk<3){
        Result->Monk = Current.Monk + 1;
        Result->Ghost = Current.Ghost;
        Result->Edge = 'A';
        return 1;
    }
    return 0;
}
int Move_2_Monks(State Current, State *Result){
    if(Current.Edge=='A'&&Current.Monk>1){
        Result->Monk = Current.Monk - 2;
        Result->Ghost = Current.Ghost;
        Result->Edge = 'B';
        return 1;
    }else if(Current.Edge=='B'&&Current.Monk<2){
        Result->Monk = Current.Monk + 2;
        Result->Ghost = Current.Ghost;
        Result->Edge = 'A';
        return 1;
    }
    return 0;
}
int Move_1_Ghost(State Current, State *Result){
    if(Current.Edge=='A'&&Current.Ghost>0){
        Result->Ghost = Current.Ghost - 1;
        Result->Monk = Current.Monk;
        Result->Edge = 'B';
        return 1;
    } else if(Current.Edge=='B'&&Current.Ghost<3){
        Result->Ghost = Current.Ghost + 1;
        Result->Monk = Current.Monk;
        Result->Edge = 'A';
        return 1;
    }
    return 0;
}
int Move_2_Ghosts(State Current, State *Result){
    if(Current.Edge=='A'&&Current.Ghost>1){
        Result->Ghost = Current.Ghost - 2;
        Result->Monk = Current.Monk;
        Result->Edge = 'B';
        return 1;
    } else if(Current.Edge=='B'&&Current.Ghost<2){
        Result->Ghost = Current.Ghost + 2;
        Result->Monk = Current.Monk;
        Result->Edge = 'A';
        return 1;
    }
    return 0;
}
int Move_1_Each_Kind(State Current, State *Result){
    if(Current.Edge=='A'&&Current.Monk>0&&Current.Ghost>0){
        Result->Monk = Current.Monk - 1;
        Result->Ghost = Current.Ghost - 1;
        Result->Edge = 'B';
        return 1;
    } else if(Current.Edge=='B'&&Current.Monk<3&&Current.Ghost<3){
        Result->Monk = Current.Monk + 1;
        Result->Ghost = Current.Ghost + 1;
        Result->Edge = 'A';
        return 1;
    }
    return 0;
}
int Calloperator(State Current, State *Result, int Option){
    switch(Option){
        case 1: return Move_1_Monk(Current,Result);
        case 2: return Move_2_Monks(Current,Result);
        case 3: return Move_1_Ghost(Current,Result);
        case 4: return Move_2_Ghosts(Current,Result);
        case 5: return Move_1_Each_Kind(Current,Result);
        default:{
            printf("Error.\n");
            return 0;
        }
    }
}
int Comparestate(State S1, State S2){
    return S1.Edge==S2.Edge && S1.Monk==S2.Monk && S1.Ghost==S2.Ghost;
}
int Findstate(State State, stack<Node*> Openstate){
    while(!Openstate.empty()){
        if(Comparestate(Openstate.top()->State,State)){
            return 1;
        }
        Openstate.pop();
    }
    return 0;
}

void Printstate(State State){
    printf("Nhà sư: %d | Hồn ma: %d | Bờ: %c.\n",State.Monk,State.Ghost,State.Edge);
}
int Valid(State State){
    if(State.Edge=='A'&&State.Ghost>State.Monk&&State.Monk!=0){
        return 0;
    }
    if(State.Edge=='A'&&State.Ghost<State.Monk&&State.Monk!=3){
        return 0;
    }
    if(State.Edge=='B'&&State.Ghost>State.Monk&&State.Monk!=0){
        return 0;
    }
    if(State.Edge=='B'&&State.Ghost<State.Monk&&State.Monk!=3){
        return 0;
    }
    return 1;
}
int Goal(State State){
    return State.Ghost==0&&State.Monk==0&&State.Edge=='B';
}
const char* Action[] = {"First state","Move one monk","Move two monks","Move one ghost","Move two ghosts","Move one each kind"};

void Print_TheWayToGetGoal(Node *N){
    stack<Node*> Stackprint;
    while(N->P!=NULL){
        Stackprint.push(N);
        N = N->P;
    }
    Stackprint.push(N);
    int Noaction = 0;
    while(!Stackprint.empty()){
        printf("Action %d: %s.\n",Noaction,Action[Stackprint.top()->Order]);
        Printstate(Stackprint.top()->State);
        Stackprint.pop();
        Noaction++;
    }
}

Node *DFS(State S){
    stack<Node*> Openstate, Closedstate;
    Node *Root = (Node*)malloc(sizeof(Node));
    Root->State = S;
    Root->P = NULL;
    Root->Order = 0;
    Openstate.push(Root);
    while(!Openstate.empty()){
        Node *NODE = Openstate.top();
        Openstate.pop();
        Closedstate.push(NODE);
        if(Goal(NODE->State)){
            Print_TheWayToGetGoal(NODE);
        }
        int Option;
        for(Option=1;Option<=5;Option++){
            State Newstate;
            Makenullstate(&Newstate);
            if(Calloperator(NODE->State,&Newstate,Option)){
                if(Findstate(Newstate,Openstate)||Findstate(Newstate,Closedstate)||!Valid(Newstate)){
                    continue;
                }
                Node *Newnode = (Node*)malloc(sizeof(Node));
                Newnode->State = Newstate;
                Newnode->P = NODE;
                Newnode->Order = Option;
                Openstate.push(Newnode);
            }
        }
    }
    return NULL;
}
int main(int argc, char const *argv[]){
   State Currentstate = {3,3,'A'};
   Node *Result = DFS(Currentstate);
}