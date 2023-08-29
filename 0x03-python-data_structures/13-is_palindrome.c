#include "lists.h"
/*
 * is_palindrome - checks if a list is plaindrome or not
 * @head: pointer to pointer to the first element
 *
 * Return: 1 if true, 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		reutrn (1);
	return (check_palindrome(head, *head));
}
/*
 * check_palindrome - checks if the elements are plaindrome
 * @head: pointer to pointer to the first element
 * @last: pointer to the element in the other half
 *
 * Return: 1 if palindrome, 0 if not
 */
int check_palindrome(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_palindrome(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
