#include "lists.h"

int main(void)
{
    listint_t *list;
    insert_node(&list, 1);
    insert_node(&list, 2);
    insert_node(&list, 2);
    insert_node(&list, 4);
    insert_node(&list, 10);
}
