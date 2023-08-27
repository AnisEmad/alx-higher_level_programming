#include "lists.h"
/*
 * insert_node - insert node into an orderd linked list
 * @head: pointer to pointer to the first element
 * @number: the number to be stored in the list
 *
 * Return: adderss of the new node
 * or null if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (current == NULL)
	{
		*head = new_node;
	}
	else
	{
		if (current->n >= number)
		{
			new_node->next = current;
			current->next = new_node;
		}
		else
		{
			while (current->next != NULL && current->next->n < number)
				current = current->next;
			new_node->next = current->next;
			current->next = new_node;
		}
	}

	return (new_node);
}
