/*Please add ; after each select statement*/
CREATE PROCEDURE contestLeaderboard()
BEGIN
    select name
    from leaderboard l inner join (
        select name, @score := @score + 1 AS rank
        from leaderboard, (select @score := 0) r
        order by score desc
    ) tmp using(name)
    where rank >= 4 and rank <=8
    order by rank
    ;

END

