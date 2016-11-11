-module(shop).
-export([cost/1]).
-export([get_shopping_list/0]).

cost(oranges)    -> 5;
cost(newspaper) -> 8;
cost(apples)    -> 2;
cost(pears)     -> 9;
cost(milk)      -> 7.

get_shopping_list() -> [{oranges,4},{newspaper,1},{apples,10},{pears,6},{milk,3}].
