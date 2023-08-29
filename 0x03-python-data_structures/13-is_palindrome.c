#include "lists.h"
/**
 * add_nodeint_begin - adds a new node at the begining of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *add_nodeint_begin(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head != NULL)
		new->next = *head;
	*head = new;
	return (new);
}
/*
 * is_palindrome - checks if a list is plaindrome or not
 * @head: pointer to pointer to the first element
 *
 * Return: 1 if true, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *new_list;
	listint_t *temp;
	int comp = 1;

	temp = *head;

	while (temp != NULL)
	{
		add_nodeint_begin(&new_list, temp->n);
		temp = temp->next;
	}
	temp = *head;
	while (temp != NULL)
	{
		if (temp->n != new_list->n)
		{
			comp = 0;
			break;
		}
		temp = temp->next;
		new_list = new_list->next;
	}
	return (comp);
}
