#include <iostream>

using namespace std;

template<typename T>
struct Node
{
	int val;
	Node* next;

    Node(T val) : val(val), next(NULL){}
    //vytiskne jeden prvek
    void print_node()
    {
        cout<<val<<endl; 
    }
    //vytiskne prvek a všechny navazující
    void print_LL()
    {
        Node* current = this;
        while (current != NULL)
        {
            cout<<current->val<<" ";
            current = current->next;
        }
        cout<<endl;
    }
    //pridá na konec listu jeden prvek
    void push_back_val(T val)
    {
        Node* current = this;
        while (current->next !=NULL)
        {
            current = current->next;
        }
        current->next = new Node(val);
    }
    //na daný index vloží prvek a všechny ostatní posune
    void insert_val(int idx, T val)
    {
        Node* current = this;
        for (int i = 0; i<idx-1; i++)
        {
            current = current->next;
        }
        Node* newNode = new Node(val);
        newNode->next = current->next;
        current->next = newNode;
    }
    //vrátí pointer na prvek, který se nachází na daném indexu
    Node* operator[](int idx)
    {
        Node* current = this;
        for (int i = 0; i<idx; i++)
        {
            current = current-> next;
        }
        return current;
    }
    //odstraní prvek na daném indexu
    void delete_node(int idx)
    {
        Node* current = this;
        Node* prev = NULL;
        for (int i = 0; i < idx; i++)
        {
            prev = current;
            current = current->next;
        }
        prev->next = current->next;
        delete current;
    }

};

int main()
{
    Node<int> LL(0);


    LL.push_back_val(1);
    LL.push_back_val(2);
    LL.push_back_val(3);

    LL.print_LL();
    LL[1]->print_node();

    LL.insert_val(2,4);
    LL.delete_node(3);
    LL.print_LL();
   	
}