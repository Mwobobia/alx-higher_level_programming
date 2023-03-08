#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current;

    /**
     * main - create list and test insert at beginning of list
     *
     * Return: Always 0.
     */
    int main(void)
    {
        listint_t *head;

        head = NULL;
        add_nodeint_end(&head, 0);
        add_nodeint_end(&head, 1);
        add_nodeint_end(&head, 2);
        add_nodeint_end(&head, 3);
        add_nodeint_end(&head, 4);
        add_nodeint_end(&head, 98);
        add_nodeint_end(&head, 402);
        add_nodeint_end(&head, 1024);
        print_listint(head);

        printf("-----------------\n");

        insert_node(&head, -7);

        print_listint(head);

        free_listint(head);

        return (0);
    }
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


    /**
     * main - create list and test insert multiple numbers
     *
     * Return: Always 0.
     */
    int main(void)
    {
        listint_t *head;

        head = NULL;
        add_nodeint_end(&head, 0);
        add_nodeint_end(&head, 1);
        add_nodeint_end(&head, 2);
        add_nodeint_end(&head, 3);
        add_nodeint_end(&head, 4);
        add_nodeint_end(&head, 98);
        add_nodeint_end(&head, 402);
        add_nodeint_end(&head, 1024);
        print_listint(head);

        printf("-----------------\n");

        insert_node(&head, 5);
        insert_node(&head, -32);
        insert_node(&head, 5432);
        insert_node(&head, 101);
        insert_node(&head, 47);
        insert_node(&head, 6405);

        print_listint(head);

        free_listint(head);

        return (0);
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

