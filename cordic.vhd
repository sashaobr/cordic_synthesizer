--------------------------------------------------------------
-- Design:  Cordic block 
-- Name:    Sasha
-- Date:    27/06/2025
--------------------------------------------------------------

library IEEE;
use IEEE.STD_Logic_1164.all;
 
entity FSM1_GOOD is
   port (clk, reset: in  std_logic;
         SlowRAM:      in  std_logic;
         Read, Write:  out std_logic);
end entity FSM1_GOOD;

architecture RTL of FSM1_GOOD is
   type StateType is (ST_Read, ST_Write, ST_Delay);
   signal CurrentState,NextState: StateType;
begin

   SEQ: process 
   begin
      wait until rising_edge(clk);
         if (reset = '1') then
            CurrentState <= ST_Read;
         else
            CurrentState <= NextState;
         end if;
   end process SEQ;

   COMB: process (CurrentState)
   begin
      case CurrentState is
         when ST_Read =>
            Read  <= '1';
            Write <= '0';
            NextState <= ST_Write;
         when ST_Write =>
            Read  <= '0';
            Write <= '1';
            if (SlowRAM = '1') then
               NextState <= ST_Delay;
            else
               NextState <= ST_Read;
            end if;
         when ST_Delay =>
            Read  <= '0';
            Write <= '0';
            NextState <= ST_Read;
         when others =>
            Read  <= '0';
            Write <= '0';
            NextState <= ST_Read;
      end case;
   end process COMB;

end architecture RTL;