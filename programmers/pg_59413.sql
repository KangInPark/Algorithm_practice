with recursive tmp as ( 
select 0 as hour
union all
select hour + 1 from tmp where hour < 23)

select hour, count(hour(a.datetime)) from tmp left join animal_outs as a on tmp.hour = hour(a.datetime) group by hour