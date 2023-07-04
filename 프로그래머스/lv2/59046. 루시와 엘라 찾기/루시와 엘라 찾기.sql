-- 코드를 입력해주세요 -- 
SELECT
  ANIMAL_ID,
  NAME,
  SEX_UPON_INTAKE
From ANIMAL_INS
Where Name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID