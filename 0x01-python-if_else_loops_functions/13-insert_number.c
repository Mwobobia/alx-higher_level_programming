#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return NULL;

    /* Fill the new node with the provided number */
    new_node->n = number;
    new_node->next = NULL;

    /* If the list is empty, insert the new node as the head */
    if (*head == NULL) {
        *head = new_node;
        return new_node;
    }

    /* Find the right place to insert the new node */
    current = *head;
    while (current->next && current->next->n < number) {
        current = current->next;
    }

    /* Insert the new node into the list */
    new_node->next = current->next;
    current->next = new_node;

    return new_node;
}

