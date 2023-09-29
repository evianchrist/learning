#include <stdio.h>

int main()
{
    // 5/2 as int
    int numi = 5/2;
    printf("%d \n", numi);

    // 5/2 as float
    float numf = 5/2;
    printf("%f \n", numf);

    /* why is 5/2 still 2 when numf is float? Because 5 and 2 are still integers so if you divide 5 by 2, then it gives you 2 */

    // 5/2 as float (2)
    float numff = (float) 5/2;
    printf("%f \n", numff);

    // printing to certain decimal point
    printf("%.2f \n", numff);

    return 0;
}