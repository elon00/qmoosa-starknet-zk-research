use starknet::ContractAddress;

#[starknet::interface]
pub trait IResearchRegistry<TContractState> {
    fn register_research(ref self: TContractState, data: felt252);
    fn get_research_data(self: @TContractState, index: u64) -> felt252;
    fn get_research_count(self: @TContractState) -> u64;
}

#[starknet::contract]
pub mod ResearchRegistry {
    use starknet::ContractAddress;
    use starknet::storage::*;

    #[storage]
    pub struct Storage {
        research_data: Vec<felt252>,
    }

    #[abi(embed_v0)]
    pub impl ResearchRegistryImpl of super::IResearchRegistry<ContractState> {
        fn register_research(ref self: ContractState, data: felt252) {
            self.research_data.append().write(data);
        }

        fn get_research_data(self: @ContractState, index: u64) -> felt252 {
            self.research_data.at(index).read()
        }

        fn get_research_count(self: @ContractState) -> u64 {
            self.research_data.len()
        }
    }
}
