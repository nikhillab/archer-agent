# src/my_project/crew.py

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import FileReadTool
import copy


from typing import List

@CrewBase
class CloudArchitectureReviewCrew():
    """Crew for Reviewing Cloud Architectures"""

    agents_config = 'config/test_agents.yaml'
    tasks_config = 'config/test_task.yaml'

    agents: List[BaseAgent]
    tasks: List[Task]
    llm_gemma3 = LLM(
        model="ollama/gemma3:4b-it-qat",
        base_url="http://localhost:11434"
    )
    # llm_gemma3 = LLM(
    #     model="ollama/deepseek-r1:1.5b",
    #     base_url="http://localhost:11434"
    # )

    # === Agents ===
    @agent
    def topology_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['topology_analyst'],
            verbose=True,
            llm=self.llm_gemma3
             
        )

    @agent
    def best_practices_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['best_practices_checker'],
            verbose=True,
            llm=self.llm_gemma3
             
        )

    @agent
    def security_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['security_reviewer'],
            verbose=True,
            llm=self.llm_gemma3
             
        )

    @agent
    def cost_efficiency_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['cost_efficiency_evaluator'],
            verbose=True,
            llm=self.llm_gemma3
             
        )

    @agent
    def interrogator(self) -> Agent:
        return Agent(
            config=self.agents_config['interrogator'],
            verbose=True,
            llm=self.llm_gemma3
             
        )

    @agent
    def summary_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['summary_generator'],
            verbose=True,
            llm=self.llm_gemma3
        )

    @task
    def topology_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['topology_analysis_task'],
            llm=self.llm_gemma3
        )

    @task
    def best_practices_check_task(self) -> Task:
        return Task(
            config=self.tasks_config['best_practices_check_task'],
            llm=self.llm_gemma3,
        )

    @task
    def security_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['security_review_task'],
            llm=self.llm_gemma3,
        )

    @task
    def cost_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['cost_analysis_task'],
            llm=self.llm_gemma3,
        )

    @task
    def interrogation_task(self) -> Task:
        return Task(
            config=self.tasks_config['interrogation_task'],
            llm=self.llm_gemma3,
        )

    @task
    def summary_task(self) -> Task:
        # dependent_task=copy.deepcopy(self.tasks)
        # dependent_task.remove()
        return Task(
            config=self.tasks_config['summary_task'],
            llm=self.llm_gemma3,
            context=[self.best_practices_check_task(),self.topology_analysis_task(),self.interrogation_task(),self.security_review_task(),self.cost_analysis_task()]
        )

    # === Crew ===
    @crew
    def crew(self) -> Crew:
        """Creates the Cloud Architecture Review Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # or parallel if you prefer
            verbose=True,
            output_log_file="logs/latest.txt",
            
        )
