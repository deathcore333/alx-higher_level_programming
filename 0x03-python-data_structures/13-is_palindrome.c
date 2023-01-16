#include "lists.h"

/**
* is_palindrome -checks if linked list is palindrome
* @head: double pointer to linked list
*
* Return: 1 if it is 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int count = 0;
	int values[1000];
	int i;

	while (current)
	{
		values[count] = current->n;
		count++;
		current = current->next;
	}
	for (i = 0; i < count / 2; i++)
	{
		if (values[i] != values[count - i - 1])
		{
			return (0);
		}
	}
	return (1);
}

