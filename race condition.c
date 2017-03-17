# include <studio.h>

lock_t casa_lock;
int val;

int casa(int *ptr, int old_val, int new_val)
{
  int flag = 0;

  LOCK(&casa_lock);
  if (*ptr == old_val)
  {
    * ptr = new_val;
    flag = 1;
  }
  UNLOCK(&casa_lock);

  return flag;
}


void producer(int id)
{
  int j;

  for (j = 0; j < id; j++)
    while (!casa(&val, val, val+1))
}


void consumer(int id){
  int j;
  for (j = 0; j < id; j++)
    while (!casa(&val, val, val-1))
}


int main(int argc, **argv){
  int i;
  val = 0;
  lock_init(&casa_lock);           /* initialize lock to "not held" status */ 
  
  for (i = 1; i <= 100; i ++)
  { 
    create_thread(producer, i);    /* create thread executing producer(i) */ 
    create_thread(consumer, i);    /* create thread executing consumer(i) */ 
  }

  start_all_threads();  /* start all threads careated above */ 
  join_all_thread();    /* wait for all threads careated above to terminate */   
  
  printf("%d\n", val);
}
